def trap(height):
    ans = 0
    st = []
    for i, h in enumerate(height):
        while st and h > height[st[-1]]:
            b_h = height[st.pop()]
            if not st:
                break
            left = st[-1]
            dh = min(height[left], h) - b_h
            ans += dh*(i-left-1)
        st.append(i)
    return ans
