class Solution:
    def floodFill(self, image, sr, sc, color):
        original = image[sr][sc]

        # If the new color is the same, nothing needs to change
        if original == color:
            return image

        def dfs(r, c):
            # Check boundaries
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]):
                return

            # Only change pixels with the original color
            if image[r][c] != original:
                return

            image[r][c] = color

            # Up
            dfs(r - 1, c)
            # Down
            dfs(r + 1, c)
            # Left
            dfs(r, c - 1)
            # Right
            dfs(r, c + 1)

        dfs(sr, sc)

        return image