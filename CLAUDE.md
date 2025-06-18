# CLAUDE.md - Development Notes and Anti-Crash Guidelines

## Game Timeout/Freeze Issues - Root Causes and Solutions

### **Critical Issues That Cause Game Timeouts:**

#### 1. **Infinite Loops in Collision Detection**
- **Problem**: Modifying lists while iterating causes index errors and infinite loops
- **Solution**: Use index-based removal with reverse iteration
- **Prevention**: Always collect indices to remove, then process in reverse order

#### 2. **Coordinate Transformation Overhead** 
- **Problem**: transform_coords() called for every draw operation causes performance bottlenecks
- **Solution**: Add bounds checking and error handling to prevent runaway calculations
- **Prevention**: Always validate scale values and add mathematical bounds checks

#### 3. **Memory Accumulation**
- **Problem**: Unlimited bullets/enemies cause memory leaks and performance degradation
- **Solution**: Strict limits on object counts (bullets: 8, enemies: 2)
- **Prevention**: Always set and enforce maximum object limits

#### 4. **Mathematical Edge Cases**
- **Problem**: Division by zero, NaN, or infinity values in calculations
- **Solution**: Wrap all math operations in try-catch blocks
- **Prevention**: Validate all inputs before mathematical operations

### **Performance Guidelines:**

#### **Object Limits (Critical)**
```python
MAX_BULLETS = 8      # Never exceed
MAX_ENEMIES = 2      # Never exceed  
MAX_STARS = 100      # Reduced from 200
```

#### **Frame Rate Control**
```python
self.set_update_rate(1/60)  # Always limit FPS
```

#### **Safe Coordinate Transformation**
```python
def transform_coords(self, x, y):
    # Always check bounds and handle errors
    if self.is_fullscreen and self.fullscreen_scale > 0:
        try:
            new_x = x * self.fullscreen_scale + self.fullscreen_offset_x
            # Bounds check to prevent runaway values
            if abs(new_x) < 100000 and not math.isnan(new_x):
                return new_x, new_y
        except (ValueError, OverflowError):
            pass
    return x, y
```

#### **Collision Detection Best Practices**
- Throttle collision checks (max 60fps)
- Use index-based removal: `for i in sorted(indices, reverse=True)`
- Always validate object existence before operations
- Add maximum iteration limits to prevent infinite loops

### **Common Timeout Patterns to Avoid:**

1. **List Modification During Iteration**
   ```python
   # WRONG - causes crashes
   for bullet in bullets:
       if condition:
           bullets.remove(bullet)
   
   # CORRECT - safe removal
   indices_to_remove = []
   for i, bullet in enumerate(bullets):
       if condition:
           indices_to_remove.append(i)
   for i in sorted(indices_to_remove, reverse=True):
       bullets.pop(i)
   ```

2. **Unbounded Mathematical Operations**
   ```python
   # WRONG - can cause infinite values
   scale = screen_height / window_height
   
   # CORRECT - with bounds checking
   try:
       scale = screen_height / window_height
       if scale <= 0 or scale > 10 or math.isnan(scale):
           scale = 1.0
   except ZeroDivisionError:
       scale = 1.0
   ```

3. **Memory Leaks from Text Objects**
   ```python
   # WRONG - creates new objects every frame
   def on_draw():
       text = arcade.Text("Hello", x, y)
       text.draw()
   
   # CORRECT - reuse or limit creation
   def __init__():
       self.text = arcade.Text("Hello", x, y)
   def on_draw():
       self.text.draw()
   ```

### **Testing Checklist Before Release:**

- [ ] Run game for 5+ minutes without timeouts
- [ ] Test fullscreen toggle multiple times
- [ ] Shoot rapidly for 30+ seconds
- [ ] Verify object counts stay within limits
- [ ] Check for memory leaks with activity monitor
- [ ] Test on both windowed and fullscreen modes

### **Emergency Debugging:**

If game starts timing out again:
1. **Check object counts** - bullets and enemies within limits?
2. **Verify coordinate transforms** - any NaN or infinite values?
3. **Review recent changes** - did new code add infinite loops?
4. **Add debug prints** - track where the freeze occurs
5. **Simplify drawing** - remove complex coordinate transformations temporarily

### **Architecture Notes:**

- **Separation of Concerns**: Keep game logic separate from rendering
- **Error Isolation**: Wrap risky operations in try-catch blocks  
- **Performance Monitoring**: Track frame times and object counts
- **Defensive Programming**: Always validate inputs and outputs

### **Development Reminders:**
- dont bash into the game. tell me when there is something to be tested and i will do it.

---

**Last Updated**: 2025-06-18  
**Game Version**: space_flight_minimal.py  
**Critical Fix Applied**: Safe coordinate transformation with bounds checking