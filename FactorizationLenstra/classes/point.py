class Point:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def __repr__(self):
        return "[%d,%d,%d]" % (self.x, self.y, self.z)