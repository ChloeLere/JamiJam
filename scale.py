## JAMIJAM
## Developed by Clovis Schneider & Chloé Lere

class Scale():
    def __init__(self, root, isMinor = False) -> None:
        self.root = root
        self.isMinor = isMinor
        self.getScale()

    def getScale(self):
        self.scale = [self.root]
        nextRoot = self.root + 12
        if self.isMinor:
            self.scale.append(self.root + 2)
            self.scale.append(self.root + 3)
            self.scale.append(self.root + 5)
            self.scale.append(self.root + 7)
            self.scale.append(self.root + 8)
            self.scale.append(self.root + 10)
            self.scale.append(nextRoot + 2)
            self.scale.append(nextRoot + 3)
            self.scale.append(nextRoot + 5)
            self.scale.append(nextRoot + 7)
            self.scale.append(nextRoot + 8)
            self.scale.append(nextRoot + 10)
            self.scale.append(nextRoot)
        else:
            self.scale.append(self.root + 2)
            self.scale.append(self.root + 4)
            self.scale.append(self.root + 5)
            self.scale.append(self.root + 7)
            self.scale.append(self.root + 9)
            self.scale.append(self.root + 11)
            self.scale.append(nextRoot)
            self.scale.append(nextRoot + 2)
            self.scale.append(nextRoot + 4)
            self.scale.append(nextRoot + 5)
            self.scale.append(nextRoot + 7)
            self.scale.append(nextRoot + 9)
            self.scale.append(nextRoot + 11)

    def getTriad(self, triad):
        return [self.scale[triad], self.scale[triad + 3], self.scale[triad + 5]]