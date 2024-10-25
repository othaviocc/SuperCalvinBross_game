import pyxel as px


def MenuPlacard():
    px.blt(36, 8, 1, 0, 175, 26, 27, 3)
    px.blt(62, 8, 1, 26, 175, 26, 27, 3)
    px.blt(88, 8, 1, 52, 175, 26, 27, 3)
    px.blt(114, 8, 1, 78, 175, 27, 27, 3)
    px.blt(141, 8, 1, 105, 175, 27, 27, 3)
    px.blt(7, 46, 1, 0, 202, 26, 27, 3)
    px.blt(33, 46, 1, 26, 202, 26, 27, 3)
    px.blt(59, 46, 1, 52, 202, 26, 27, 3)
    px.blt(129, 46, 1, 78, 202, 26, 27, 3)
    px.blt(155, 46, 1, 80, 229, 24, 27, 3)
    px.blt(179, 46, 1, 54, 229, 26, 27, 3)
    px.blt(53, 84, 1, 0, 229, 27, 27, 3)
    px.blt(80, 84, 1, 105, 175, 27, 27, 3)
    px.blt(107, 84, 1, 27, 229, 27, 27, 3)
    px.blt(134, 84, 1, 0, 175, 26, 27, 3)


class SuperCalvinBros:
    def __init__(self):
        px.init(width=213, height=120, title='Super Calvin Bros', fps=60, quit_key=px.KEY_Q)
        px.image(0).load(0, 0, 'maincharacter.png')
        px.image(1).load(0, 0, 'tileset.png')
        px.image(2).load(0, 0, 'mobs.png')
        px.fullscreen(True)
        # Menu
        self.start = False
        self.darkBack1 = False
        self.darkBack2 = False
        self.darkBack3 = False
        self.chooseDifficulty = False
        self.difficulty = -1
        # BackGround
        self.x = 0
        self.corner = True
        self.physics = False
        self.protection = False
        self.minY = 80
        self.pause = False
        # Player
        self.playerAnimation = 0
        self.playerAnimationVariable = 0
        self.playerWay = 0
        self.playerX = 10
        self.playerY = 80
        self.canWalkRight = True
        self.canWalkLeft = True
        self.alive = True
        self.lava = False
        self.playerOnFire = 32
        self.deathJump = True
        # Pulo
        self.mustJump = False
        self.canJump = True
        self.jump = 28
        self.fallFrames = 0
        self.fall = False
        self.canFall = False
        self.fallWhenLeavePhysics = False
        self.mustFall = False
        self.falling = False
        self.cantJumpProtection = False
        # Mobs
        self.mobsAnimation = 0
        self.mobsAnimationVariable = 0
        self.mobsWay = 0
        self.mobsSpeed = 0
        self.mobsDisplacement1 = 103
        self.mobsDisplacement2 = 271
        self.mobsDisplacement3 = 591
        self.mobsDisplacement4 = 768
        self.mobsDisplacement5 = 1128
        self.mobsStaticDisplacement = 0
        self.endermanHead1 = 0
        self.endermanHead2 = 0
        self.endermanHead3 = 0
        self.endermanHead4 = 0
        self.endermanHead5 = 0
        # Fase
        self.passLevel = 0

        # Blocos
        self.lavaAnimationVariable = 0
        self.lavaAnimation = 0
        # Run
        px.run(self.Update, self.Draw)

    def Update(self):
        if not self.start:
            self.MenuScreenInteractions()
        else:
            px.mouse(False)
            self.Pause()
            if not self.pause:
                self.Physics()
                self.Walk()
                self.Jump()
                self.Fall()
                self.Protection()
                self.Die()
                self.Corner()
                self.PassLevel()
                self.MobsAnimation()
                self.MobsLim(186)
                self.LavaAnimation()

    def MenuScreenInteractions(self):
        if not self.chooseDifficulty:
            px.mouse(True)
            if 97 <= px.mouse_x <= 115 and 46 <= px.mouse_y <= 54:
                if px.btnp(px.MOUSE_BUTTON_LEFT, repeat=True):
                    self.darkBack1 = True
                elif px.btnr(px.MOUSE_BUTTON_LEFT):
                    self.darkBack1 = False
                    self.chooseDifficulty = True
            elif 97 <= px.mouse_x <= 115 and 65 <= px.mouse_y <= 73:
                if px.btnp(px.MOUSE_BUTTON_LEFT, repeat=True):
                    self.darkBack2 = True
                elif px.btnr(px.MOUSE_BUTTON_LEFT):
                    px.quit()
            else:
                self.darkBack1 = False
                self.darkBack2 = False
        elif self.chooseDifficulty:
            if (97 <= px.mouse_x <= 115) and (41 <= px.mouse_y <= 49):
                if px.btnp(px.MOUSE_BUTTON_LEFT, repeat=True):
                    self.darkBack1 = True
                elif px.btnr(px.MOUSE_BUTTON_LEFT):
                    self.darkBack1 = False
                    self.difficulty = 0
                    self.start = True
            elif (93 <= px.mouse_x <= 119) and (55 <= px.mouse_y <= 63):
                if px.btnp(px.MOUSE_BUTTON_LEFT, repeat=True):
                    self.darkBack2 = True
                elif px.btnr(px.MOUSE_BUTTON_LEFT):
                    self.darkBack2 = False
                    self.difficulty = 1
                    self.start = True
            elif (97 <= px.mouse_x <= 115) and (69 <= px.mouse_y <= 77):
                if px.btnp(px.MOUSE_BUTTON_LEFT, repeat=True):
                    self.darkBack3 = True
                elif px.btnr(px.MOUSE_BUTTON_LEFT):
                    self.darkBack3 = False
                    self.difficulty = 2
                    self.start = True
            else:
                self.darkBack1 = False
                self.darkBack2 = False
                self.darkBack3 = False

    def MenuScreen(self):
        if not self.chooseDifficulty:
            px.cls(1)
            MenuPlacard()
            px.rectb(97, 46, 19, 9, 0)
            if self.darkBack1:
                px.rect(97, 46, 19, 9, 0)
            px.text(99, 48, 'PLAY', 7)
            px.rectb(97, 65, 19, 9, 0)
            if self.darkBack2:
                px.rect(97, 65, 19, 9, 0)
            px.text(99, 67, 'QUIT', 7)
        elif self.chooseDifficulty:
            px.cls(1)
            MenuPlacard()
            px.rectb(97, 41, 19, 9, 0)
            if self.darkBack1:
                px.rect(97, 41, 19, 9, 0)
            px.text(99, 43, 'EASY', 7)
            px.rectb(93, 55, 27, 9, 0)
            if self.darkBack2:
                px.rect(93, 55, 27, 9, 0)
            px.text(95, 57, 'MEDIUM', 7)
            px.rectb(97, 69, 19, 9, 0)
            if self.darkBack3:
                px.rect(97, 69, 19,  9, 0)
            px.text(99, 71, 'HARD', 7)

    def Pause(self):
        if self.alive:
            if px.btnr(px.KEY_ESCAPE) and self.pause:
                self.pause = False
            elif px.btnr(px.KEY_ESCAPE):
                self.pause = True

    def PauseScreen(self):
        if self.pause:
            px.text(83, 48, "Jogo Pausado", 0)
            px.text(77, 57, "ESC - Despausar", 0)
            px.text(91, 66, "Q - Quit", 0)

    def Physics(self):
        if self.passLevel == 0:
            if self.x == -1387:
                # Obsidian
                if 181 >= self.playerX > 128:
                    self.canFall = False
                    self.fallWhenLeavePhysics = True
                    self.minY = 64
                else:
                    self.canFall = True
                    self.fallWhenLeavePhysics = False
                    self.minY = 80
                if ((px.btnp(px.KEY_D, repeat=True) or px.btnp(px.KEY_RIGHT, repeat=True)) and
                        self.playerY > 64 and self.playerX == 128
                ):
                    self.physics = True
                    self.canWalkRight = False
                elif ((px.btnp(px.KEY_A, repeat=True) or px.btnp(px.KEY_LEFT, repeat=True)) and
                      self.playerY > 64 and self.playerX == 182
                ):
                    self.physics = True
                    self.canWalkLeft = False
                else:
                    self.physics = False
                    self.canWalkRight = True
                    self.canWalkLeft = True
            elif 1071 < abs(self.x) < 1358:
                # Brick
                if 1072 < abs(self.x) <= 1088:
                    self.canFall = False
                    self.fallWhenLeavePhysics = True
                    self.minY = 64
                elif 1088 < abs(self.x) < 1118:
                    self.canFall = False
                    self.fallWhenLeavePhysics = True
                    self.minY = 48
                elif 1139 < abs(self.x) < 1159:
                    self.canFall = False
                    self.fallWhenLeavePhysics = True
                    self.minY = 32
                elif 1182 < abs(self.x) < 1202:
                    self.canFall = False
                    self.fallWhenLeavePhysics = True
                    self.minY = 32
                elif 1225 < abs(self.x) < 1245:
                    self.canFall = False
                    self.fallWhenLeavePhysics = True
                    self.minY = 32
                elif 1268 < abs(self.x) < 1288:
                    self.canFall = False
                    self.fallWhenLeavePhysics = True
                    self.minY = 32
                elif 1310 < abs(self.x) < 1341:
                    self.canFall = False
                    self.fallWhenLeavePhysics = True
                    self.minY = 48
                elif 1341 <= abs(self.x) < 1357:
                    self.canFall = False
                    self.fallWhenLeavePhysics = True
                    self.minY = 64
                else:
                    self.canFall = True
                    self.fallWhenLeavePhysics = False
                    self.minY = 80
                if ((px.btnp(px.KEY_D, repeat=True) or px.btnp(px.KEY_RIGHT, repeat=True)) and
                        self.x == -1072 and self.playerY > 64
                ):
                    self.physics = True
                    self.canWalkRight = False
                elif ((px.btnp(px.KEY_D, repeat=True) or px.btnp(px.KEY_RIGHT, repeat=True)) and
                      self.x == -1088 and self.playerY > 48
                ):
                    self.physics = True
                    self.canWalkRight = False
                elif ((px.btnp(px.KEY_A, repeat=True) or px.btnp(px.KEY_LEFT, repeat=True)) and
                      self.x == -1118 and self.playerY > 48
                ):
                    self.physics = True
                    self.canWalkLeft = False

                elif ((px.btnp(px.KEY_D, repeat=True) or px.btnp(px.KEY_RIGHT, repeat=True)) and
                      self.x == -1139 and 32 < self.playerY < 80
                ):
                    self.physics = True
                    self.canWalkRight = False
                elif ((px.btnp(px.KEY_A, repeat=True) or px.btnp(px.KEY_LEFT, repeat=True)) and
                      self.x == -1159 and 32 < self.playerY < 80
                ):
                    self.physics = True
                    self.canWalkLeft = False

                elif ((px.btnp(px.KEY_D, repeat=True) or px.btnp(px.KEY_RIGHT, repeat=True)) and
                      self.x == -1182 and 32 < self.playerY < 80
                ):
                    self.physics = True
                    self.canWalkRight = False
                elif ((px.btnp(px.KEY_A, repeat=True) or px.btnp(px.KEY_LEFT, repeat=True)) and
                      self.x == -1202 and 32 < self.playerY < 80
                ):
                    self.physics = True
                    self.canWalkLeft = False

                elif ((px.btnp(px.KEY_D, repeat=True) or px.btnp(px.KEY_RIGHT, repeat=True)) and
                      self.x == -1225 and 32 < self.playerY < 80
                ):
                    self.physics = True
                    self.canWalkRight = False
                elif ((px.btnp(px.KEY_A, repeat=True) or px.btnp(px.KEY_LEFT, repeat=True)) and
                      self.x == -1245 and 32 < self.playerY < 80
                ):
                    self.physics = True
                    self.canWalkLeft = False

                elif ((px.btnp(px.KEY_D, repeat=True) or px.btnp(px.KEY_RIGHT, repeat=True)) and
                      self.x == -1268 and 32 < self.playerY < 80
                ):
                    self.physics = True
                    self.canWalkRight = False
                elif ((px.btnp(px.KEY_A, repeat=True) or px.btnp(px.KEY_LEFT, repeat=True)) and
                      self.x == -1288 and 32 < self.playerY < 80
                ):
                    self.physics = True
                    self.canWalkLeft = False

                elif ((px.btnp(px.KEY_D, repeat=True) or px.btnp(px.KEY_RIGHT, repeat=True)) and
                      self.x == -1310 and self.playerY > 48
                ):
                    self.physics = True
                    self.canWalkRight = False
                elif ((px.btnp(px.KEY_A, repeat=True) or px.btnp(px.KEY_LEFT, repeat=True)) and
                      self.x == -1341 and self.playerY > 48
                ):
                    self.physics = True
                    self.canWalkLeft = False

                elif ((px.btnp(px.KEY_A, repeat=True) or px.btnp(px.KEY_LEFT, repeat=True)) and
                      self.x == -1357 and self.playerY > 64
                ):
                    self.physics = True
                    self.canWalkLeft = False
                else:
                    self.physics = False
                    self.canWalkRight = True
                    self.canWalkLeft = True
        elif self.passLevel == 1:
            # LavaFloor
            if 549 <= abs(self.x) <= 684:
                if 551 <= abs(self.x) <= 602:
                    self.minY = 136
                    if self.playerY == 80:
                        self.mustFall = True
                elif 630 <= abs(self.x) <= 681:
                    self.minY = 136
                    if self.playerY == 80:
                        self.mustFall = True
                else:
                    self.minY = 80
            elif self.x == -1387:
                if 112 < self.playerX < 180:
                    self.canFall = False
                    self.fallWhenLeavePhysics = True
                    self.minY = 69
                else:
                    self.canFall = True
                    self.fallWhenLeavePhysics = False
                    self.minY = 80
                if ((px.btnp(px.KEY_D, repeat=True) or px.btnp(px.KEY_RIGHT, repeat=True)) and
                        (self.playerX == 112) and self.playerY > 69
                ):
                    self.physics = True
                    self.canWalkRight = False
                elif ((px.btnp(px.KEY_A, repeat=True) or px.btnp(px.KEY_LEFT, repeat=True)) and
                      (self.playerX == 180) and self.playerY > 69
                ):
                    self.physics = True
                    self.canWalkLeft = False
                else:
                    self.physics = False
                    self.canWalkRight = True
                    self.canWalkLeft = True
        elif self.passLevel == 2:
            if self.x == -1387:
                if 112 < self.playerX < 180:
                    self.canFall = False
                    self.fallWhenLeavePhysics = True
                    self.minY = 69
                else:
                    self.canFall = True
                    self.fallWhenLeavePhysics = False
                    self.minY = 80
                if ((px.btnp(px.KEY_D, repeat=True) or px.btnp(px.KEY_RIGHT, repeat=True)) and
                        self.playerX == 112 and self.playerY > 69
                ):
                    self.physics = True
                    self.canWalkRight = False
                elif ((px.btnp(px.KEY_A, repeat=True) or px.btnp(px.KEY_LEFT, repeat=True)) and
                      self.playerX == 180 and self.playerY > 69
                ):
                    self.physics = True
                    self.canWalkLeft = False
                else:
                    self.physics = False
                    self.canWalkRight = True
                    self.canWalkLeft = True
            if 610 <= abs(self.x) <= 900:
                if 678 <= abs(self.x) <= 780:
                    if 679 <= abs(self.x) <= 743:
                        self.minY = 136
                        if self.playerY == 80:
                            self.mustFall = True
                    else:
                        self.minY = 80
                elif 630 < abs(self.x) <= 646:
                    self.canFall = False
                    self.fallWhenLeavePhysics = True
                    self.minY = 64
                elif 646 < abs(self.x) < 676:
                    self.canFall = False
                    self.fallWhenLeavePhysics = True
                    self.minY = 48
                else:
                    self.canFall = True
                    self.fallWhenLeavePhysics = False
                    self.minY = 80
                if ((px.btnp(px.KEY_D, repeat=True) or px.btnp(px.KEY_RIGHT, repeat=True)) and
                        self.x == -630 and self.playerY > 64
                ):
                    self.physics = True
                    self.canWalkRight = False
                elif ((px.btnp(px.KEY_D, repeat=True) or px.btnp(px.KEY_RIGHT, repeat=True)) and
                        self.x == -646 and self.playerY > 48
                ):
                    self.physics = True
                    self.canWalkRight = False
                elif ((px.btnp(px.KEY_A, repeat=True) or px.btnp(px.KEY_LEFT, repeat=True)) and
                      self.x == -676 and self.playerY > 48
                ):
                    self.physics = True
                    self.canWalkLeft = False
                elif 744 <= abs(self.x) <= 780 and self.playerY > 80:
                    self.minY = 136
                    self.canWalkRight = False
                elif 744 <= abs(self.x) <= 780 and self.playerY > 80:
                    self.minY = 136
                    self.canWalkRight = False
                else:
                    self.physics = False
                    self.canWalkRight = True
                    self.canWalkLeft = True
            else:
                if ((134 <= abs(self.x) <= 203 or 288 <= abs(self.x) <= 357 or 461 <= abs(self.x) <= 530 or
                     980 <= abs(self.x) <= 1049 or 1256 <= abs(self.x) <= 1325)
                ):
                    self.cantJumpProtection = True
                    if self.playerY < 80:
                        self.physics = True
                        self.canWalkRight = False
                        self.canWalkLeft = False
                    else:
                        self.physics = False
                        self.canWalkRight = True
                        self.canWalkLeft = True
                else:
                    self.cantJumpProtection = False

    def Walk(self):
        if self.alive:
            if px.btnp(px.KEY_D, repeat=True) or px.btnp(px.KEY_RIGHT, repeat=True) or px.btnp(
                    px.KEY_A, repeat=True) or px.btnp(px.KEY_LEFT, repeat=True
            ):
                self.playerAnimationVariable += 1
            if (not px.btnp(px.KEY_D, repeat=True) and not px.btnp(px.KEY_RIGHT, repeat=True)) and (
                    not px.btnp(px.KEY_A, repeat=True) and not px.btnp(px.KEY_LEFT, repeat=True)
            ):
                self.mobsSpeed = 0
                self.playerAnimation = 0
                self.playerAnimationVariable = 0
            if self.playerAnimationVariable == 48:
                self.playerAnimationVariable = 0
            if (px.btnp(px.KEY_D, repeat=True) or
                    px.btnp(px.KEY_RIGHT, repeat=True)
            ):
                self.Animation()
                if self.canWalkRight:
                    self.mobsSpeed = 1
                    self.playerWay = 0
                    if self.playerX == 53:
                        if self.x > -1387:
                            self.x -= 1
            elif px.btnp(px.KEY_A, repeat=True) or px.btnp(px.KEY_LEFT, repeat=True):
                self.Animation()
                if self.canWalkLeft:
                    self.mobsSpeed = 2
                    self.playerWay = 32
                    if self.playerX == 53:
                        if self.x < 0:
                            self.x += 1

    def Animation(self):
        if self.alive:
            if 0 <= self.playerAnimationVariable < 2:
                self.playerAnimation = 0
            elif 2 <= self.playerAnimationVariable < 4:
                self.playerAnimation = 21
            elif 4 <= self.playerAnimationVariable < 7:
                self.playerAnimation = 42
            elif 7 <= self.playerAnimationVariable < 11 or 39 <= self.playerAnimationVariable < 43:
                self.playerAnimation = 63
            elif 11 <= self.playerAnimationVariable < 16 or 34 <= self.playerAnimationVariable < 39:
                self.playerAnimation = 84
            elif 16 <= self.playerAnimationVariable < 22 or 28 <= self.playerAnimationVariable < 34:
                self.playerAnimation = 105
            elif 22 <= self.playerAnimationVariable < 28:
                self.playerAnimation = 126
            elif 46 <= self.playerAnimationVariable < 48:
                self.playerAnimation = 147
            elif 43 <= self.playerAnimationVariable < 46:
                self.playerAnimation = 168

    def Jump(self):
        framesToJump = [7, 10, 12, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
        if (px.btn(px.KEY_W) or px.btn(px.KEY_UP)) and self.canJump and self.alive and not self.falling and not self.cantJumpProtection:
            self.mustJump = True
        if self.mustJump:
            self.canJump = False
            self.jump -= 1
            if self.jump == 0:
                self.fall = True
                self.mustJump = False
                self.jump = 28
            if self.jump in framesToJump:
                self.playerY -= 1
        if not self.alive and self.deathJump:
            self.fallFrames = 0
            self.minY = 160
            self.playerWay = 0
            self.playerAnimation = 189
            if self.lava:
                self.playerY -= 10
                self.playerAnimation = 210
                self.playerOnFire = 42
            self.fall = False
            self.mustFall = False
            self.jump = 28
            self.mustJump = True
            self.deathJump = False

    def Fall(self):
        framesToFall = [7, 10, 12, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
        framesToFall2x = []
        for i in range(28, 172):
            framesToFall2x.append(i)
        if self.fall or self.mustFall:
            self.falling = True
            if self.playerY < self.minY:
                self.fallFrames += 1
                if self.fallFrames in framesToFall:
                    self.playerY += 1
                    if self.playerY > 80 and self.lava:
                        self.playerY -= 0.5
                elif self.fallFrames in framesToFall2x:
                    self.playerY += 2
                    if self.playerY > 80 and self.lava:
                        self.playerY -= 1.5
                elif not self.alive and self.fallFrames == 83:
                    self.fallFrames = 28
            elif self.playerY == self.minY and self.alive:
                self.falling = False
                self.fallFrames = 0
                self.fall = False
                self.canJump = True
                self.mustFall = False
        if self.fallWhenLeavePhysics:
            self.mustFall = True
        if self.mustJump:
            self.mustFall = False

    def Protection(self):
        if self.passLevel == 0:
            if (188 <= abs(self.x) <= 196 or 356 <= abs(self.x) <= 364 or
                    684 <= abs(self.x) <= 692 or 868 <= abs(self.x) <= 876
            ):
                self.protection = True
            else:
                self.protection = False
        elif self.passLevel == 1:
            if (164 <= abs(self.x) <= 172 or 383 <= abs(self.x) <= 391 or
                    964 <= abs(self.x) <= 972 or 1316 <= abs(self.x) <= 1324
            ):
                self.protection = True
            else:
                self.protection = False
        elif self.passLevel == 2:
            if (148 <= abs(self.x) <= 188 or 302 <= abs(self.x) <= 342 or 475 <= abs(self.x) <= 515 or
                    993 <= abs(self.x) <= 1033 or 1270<= abs(self.x) <= 1310
            ):
                self.protection = True
            else:
                self.protection = False

    def Die(self):
        if not self.corner and not self.protection:
            if ((0 <= self.mobsDisplacement1 <= 13 or 0 <= self.mobsDisplacement2 <= 13 or
                0 <= self.mobsDisplacement3 <= 13 or 0 <= self.mobsDisplacement4 <= 13 or
                0 <= self.mobsDisplacement5 <= 13) and self.playerY >= 50
            ):
                self.alive = False
            if self.playerY > 80 and self.alive:
                self.alive = False
                self.deathJump = False
                if self.passLevel == 1:
                    self.lava = True
                    self.deathJump = True
        if not self.alive:
            if px.btn(px.KEY_SPACE):
                # Fase
                if self.difficulty == 1 or self.difficulty == 2:
                    self.passLevel = 0
                # BackGround
                self.x = 0
                self.corner = True
                self.physics = False
                self.protection = False
                self.minY = 80
                self.pause = False
                # Player
                self.playerAnimation = 0
                self.playerAnimationVariable = 0
                self.playerWay = 0
                self.playerX = 10
                self.playerY = 80
                self.canWalkRight = True
                self.canWalkLeft = True
                self.alive = True
                self.lava = False
                self.playerOnFire = 32
                self.deathJump = True
                # Pulo
                self.mustJump = False
                self.canJump = True
                self.jump = 28
                self.fallFrames = 0
                self.fall = False
                self.canFall = False
                self.fallWhenLeavePhysics = False
                self.mustFall = False
                self.falling = False
                self.cantJumpProtection = False
                # Mobs
                self.mobsAnimation = 0
                self.mobsAnimationVariable = 0
                self.mobsWay = 0
                self.mobsSpeed = 0
                if self.passLevel == 0:
                    self.mobsDisplacement1 = 103
                    self.mobsDisplacement2 = 271
                    self.mobsDisplacement3 = 591
                    self.mobsDisplacement4 = 768
                    self.mobsDisplacement5 = 1128
                elif self.passLevel == 1:
                    self.mobsDisplacement1 = 76
                    self.mobsDisplacement2 = 295
                    self.mobsDisplacement3 = 872
                    self.mobsDisplacement4 = 1230
                    self.mobsDisplacement5 = 2000
                elif self.passLevel == 2:
                    self.mobsDisplacement1 = 82
                    self.mobsDisplacement2 = 236
                    self.mobsDisplacement3 = 409
                    self.mobsDisplacement4 = 928
                    self.mobsDisplacement5 = 1204
                self.mobsStaticDisplacement = 0

    def Corner(self):
        if self.alive:
            if self.x == 0:
                self.corner = True
                if px.btnp(px.KEY_A, repeat=True) or px.btnp(px.KEY_LEFT, repeat=True):
                    if self.canWalkLeft:
                        self.playerX -= 1
                        if self.playerX == -1:
                            self.playerX = 0
                if px.btnp(px.KEY_D, repeat=True) or px.btnp(px.KEY_RIGHT, repeat=True):
                    if self.canWalkRight:
                        self.playerX += 1
            elif self.x == -1387:
                self.corner = True
                if px.btnp(px.KEY_A, repeat=True) or px.btnp(px.KEY_LEFT, repeat=True):
                    if self.canWalkLeft:
                        self.playerX -= 1
                if px.btnp(px.KEY_D, repeat=True) or px.btnp(px.KEY_RIGHT, repeat=True):
                    if self.canWalkRight:
                        self.playerX += 1
                        if self.playerX == 193:
                            self.playerX = 192
            else:
                self.corner = False

    def PassLevel(self):
        if self.alive:
            if px.btn(px.KEY_K) and ((self.passLevel == 0 and (self.x == -1387 and (
                    166 >= self.playerX >= 142) and self.playerY <= 64)) or (
                    (self.passLevel == 1 or self.passLevel == 2) and (
                    self.x == -1387 and (179 >= self.playerX >= 113) and self.playerY <= 69))
            ):
                # BackGround
                self.x = 0
                self.corner = True
                self.physics = False
                self.protection = False
                self.minY = 80
                self.pause = False
                # Player
                self.playerAnimation = 0
                self.playerAnimationVariable = 0
                self.playerWay = 0
                self.playerX = 10
                self.playerY = 80
                self.canWalkRight = True
                self.canWalkLeft = True
                self.alive = True
                self.lava = False
                self.playerOnFire = 32
                self.deathJump = True
                # Pulo
                self.mustJump = False
                self.canJump = True
                self.jump = 28
                self.fallFrames = 0
                self.fall = False
                self.canFall = False
                self.fallWhenLeavePhysics = False
                self.mustFall = False
                self.falling = False
                self.cantJumpProtection = False
                # Mobs
                self.mobsAnimation = 0
                self.mobsAnimationVariable = 0
                self.mobsWay = 0
                self.mobsSpeed = 0
                if self.passLevel == 0:
                    self.mobsDisplacement1 = 76
                    self.mobsDisplacement2 = 295
                    self.mobsDisplacement3 = 872
                    self.mobsDisplacement4 = 1230
                    self.mobsDisplacement5 = 2000
                elif self.passLevel == 1:
                    self.mobsDisplacement1 = 82
                    self.mobsDisplacement2 = 236
                    self.mobsDisplacement3 = 409
                    self.mobsDisplacement4 = 928
                    self.mobsDisplacement5 = 1204
                elif self.passLevel == 2:
                    self.mobsDisplacement1 = -1 
                    self.mobsDisplacement1 = -1
                    self.mobsDisplacement1 = -1
                    self.mobsDisplacement1 = -1
                    self.mobsDisplacement1 = -1
                self.mobsStaticDisplacement = 0
                # Fase
                self.passLevel += 1
            elif px.btn(px.KEY_K) and self.passLevel == 3 and 142 <= self.playerX <= 150:
                self.passLevel = 4

    def Victory(self):
        px.cls(0)
        self.House()
        self.Land(112, 0, 8)
        self.Cloud()
        self.Tree(248)
        self.Tree(416)
        self.Tree(744)
        self.Tree(928)
        px.blt(self.playerX, self.playerY, 0, self.playerAnimation, self.playerWay, 21, self.playerOnFire, 0)
        self.PauseScreen()
        px.text(87, 54, "Parabens!", px.frame_count % 16)
        px.text(83, 60, "Voce ganhou!", px.frame_count % 16)


    def MobsAnimation(self):
        if self.alive:
            if self.passLevel == 0:
                if self.mobsAnimationVariable == 40:
                    self.mobsAnimationVariable = 0
                self.mobsAnimationVariable += 1
                if 0 <= self.mobsAnimationVariable < 10:
                    self.mobsAnimation = 0
                elif (10 <= self.mobsAnimationVariable < 20) or (30 <= self.mobsAnimationVariable < 40):
                    self.mobsAnimation = 14
                elif 20 <= self.mobsAnimationVariable < 30:
                    self.mobsAnimation = 28
            elif self.passLevel == 1:
                if self.mobsAnimationVariable == 160:
                    self.mobsAnimationVariable = 0
                self.mobsAnimationVariable += 1
                if 0 <= self.mobsAnimationVariable < 10:
                    self.mobsAnimation = 0
                elif 10 <= self.mobsAnimationVariable < 20:
                    self.mobsAnimation = 16
                elif 20 <= self.mobsAnimationVariable < 30:
                    self.mobsAnimation = 32
                elif 30 <= self.mobsAnimationVariable < 40:
                    self.mobsAnimation = 48
                elif 40 <= self.mobsAnimationVariable < 50:
                    self.mobsAnimation = 64
                elif 50 <= self.mobsAnimationVariable < 60:
                    self.mobsAnimation = 80
                elif 60 <= self.mobsAnimationVariable < 70:
                    self.mobsAnimation = 96
                elif 70 <= self.mobsAnimationVariable < 80:
                    self.mobsAnimation = 112
                elif 80 <= self.mobsAnimationVariable < 90:
                    self.mobsAnimation = 128
                elif 90 <= self.mobsAnimationVariable < 100:
                    self.mobsAnimation = 144
                elif 100 <= self.mobsAnimationVariable < 110:
                    self.mobsAnimation = 160
                elif 110 <= self.mobsAnimationVariable < 120:
                    self.mobsAnimation = 176
                elif 120 <= self.mobsAnimationVariable < 130:
                    self.mobsAnimation = 192
                elif 130 <= self.mobsAnimationVariable < 140:
                    self.mobsAnimation = 208
                elif 140 <= self.mobsAnimationVariable < 150:
                    self.mobsAnimation = 224
                elif 150 <= self.mobsAnimationVariable < 160:
                    self.mobsAnimation = 240
            elif self.passLevel == 2:
                if self.mobsWay == 0:
                    if self.mobsDisplacement1 < 0:
                        self.endermanHead1 = 8
                    else:
                        self.endermanHead1 = 0
                    if self.mobsDisplacement2 < 0:
                        self.endermanHead2 = 8
                    else:
                        self.endermanHead2 = 0
                    if self.mobsDisplacement3 < 0:
                        self.endermanHead3 = 8
                    else:
                        self.endermanHead3 = 0
                    if self.mobsDisplacement4 < 0:
                        self.endermanHead4 = 8
                    else:
                        self.endermanHead4 = 0
                    if self.mobsDisplacement5 < 0:
                        self.endermanHead5 = 8
                    else:
                        self.endermanHead5 = 0
                elif self.mobsWay == 1:
                    if self.mobsDisplacement1 > 13:
                        self.endermanHead1 = 8
                    else:
                        self.endermanHead1 = 0
                    if self.mobsDisplacement2 > 13:
                        self.endermanHead2 = 8
                    else:
                        self.endermanHead2 = 0
                    if self.mobsDisplacement3 > 13:
                        self.endermanHead3 = 8
                    else:
                        self.endermanHead3 = 0
                    if self.mobsDisplacement4 > 13:
                        self.endermanHead4 = 8
                    else:
                        self.endermanHead4 = 0
                    if self.mobsDisplacement5 > 13:
                        self.endermanHead5 = 8
                    else:
                        self.endermanHead5 = 0
                else:
                    self.endermanHead = 0
                if self.mobsAnimationVariable == 120:
                    self.mobsAnimationVariable = 0
                self.mobsAnimationVariable += 1
                if 0 <= self.mobsAnimationVariable < 10:
                    self.mobsAnimation = 0
                elif (10 <= self.mobsAnimationVariable < 20) or (110 <= self.mobsAnimationVariable < 120):
                    self.mobsAnimation = 26
                elif 20 <= self.mobsAnimationVariable < 30 or (100 <= self.mobsAnimationVariable < 110):
                    self.mobsAnimation = 52
                elif (30 <= self.mobsAnimationVariable < 40) or (90 <= self.mobsAnimationVariable < 100):
                    self.mobsAnimation = 78
                elif (40 <= self.mobsAnimationVariable < 50) or (80 <= self.mobsAnimationVariable < 90):
                    self.mobsAnimation = 104
                elif (50 <= self.mobsAnimationVariable < 60) or (70 <= self.mobsAnimationVariable < 80):
                    self.mobsAnimation = 130
                elif 60 <= self.mobsAnimationVariable < 70:
                    self.mobsAnimation = 156


    def MobsLim(self, displacement):
        if self.alive and self.passLevel != 3:
            if self.difficulty == 2 and self.passLevel != 2:
                a = 1
            else:
                a = 0
            if self.corner:
                if self.mobsStaticDisplacement >= displacement:
                    self.mobsWay = 1
                elif self.mobsStaticDisplacement <= 0:
                    self.mobsWay = 0
                if self.mobsWay == 0:
                    self.mobsStaticDisplacement += 1 + a
                    self.mobsDisplacement1 += 1 + a
                    self.mobsDisplacement2 += 1 + a
                    self.mobsDisplacement3 += 1 + a
                    self.mobsDisplacement4 += 1 + a
                    self.mobsDisplacement5 += 1 + a
                elif self.mobsWay == 1:
                    self.mobsStaticDisplacement = self.mobsStaticDisplacement - 1 - a
                    self.mobsDisplacement1 = self.mobsDisplacement1 - 1 - a
                    self.mobsDisplacement2 = self.mobsDisplacement2 - 1 - a
                    self.mobsDisplacement3 = self.mobsDisplacement3 - 1 - a
                    self.mobsDisplacement4 = self.mobsDisplacement4 - 1 - a
                    self.mobsDisplacement5 = self.mobsDisplacement5 - 1 - a
            elif not self.corner:
                if self.mobsStaticDisplacement >= displacement:
                    self.mobsWay = 1
                elif self.mobsStaticDisplacement <= 0:
                    self.mobsWay = 0
                if self.mobsWay == 0:
                    self.mobsStaticDisplacement += 1 + a
                    if self.mobsSpeed == 0 or self.physics:
                        self.mobsDisplacement1 += 1 + a
                        self.mobsDisplacement2 += 1 + a
                        self.mobsDisplacement3 += 1 + a
                        self.mobsDisplacement4 += 1 + a
                        self.mobsDisplacement5 += 1 + a
                    elif self.mobsSpeed == 1 and not self.physics:
                        self.mobsDisplacement1 += 0 + a
                        self.mobsDisplacement2 += 0 + a
                        self.mobsDisplacement3 += 0 + a
                        self.mobsDisplacement4 += 0 + a
                        self.mobsDisplacement5 += 0 + a
                    elif self.mobsSpeed == 2 and not self.physics:
                        self.mobsDisplacement1 += 2 + a
                        self.mobsDisplacement2 += 2 + a
                        self.mobsDisplacement3 += 2 + a
                        self.mobsDisplacement4 += 2 + a
                        self.mobsDisplacement5 += 2 + a
                elif self.mobsWay == 1:
                    self.mobsStaticDisplacement = self.mobsStaticDisplacement - 1 - a
                    if self.mobsSpeed == 0 or self.physics:
                        self.mobsDisplacement1 = self.mobsDisplacement1 - 1 - a
                        self.mobsDisplacement2 = self.mobsDisplacement2 - 1 - a
                        self.mobsDisplacement3 = self.mobsDisplacement3 - 1 - a
                        self.mobsDisplacement4 = self.mobsDisplacement4 - 1 - a
                        self.mobsDisplacement5 = self.mobsDisplacement5 - 1 - a
                    elif self.mobsSpeed == 1 and not self.physics:
                        self.mobsDisplacement1 = self.mobsDisplacement1 - 2 - a
                        self.mobsDisplacement2 = self.mobsDisplacement2 - 2 - a
                        self.mobsDisplacement3 = self.mobsDisplacement3 - 2 - a
                        self.mobsDisplacement4 = self.mobsDisplacement4 - 2 - a
                        self.mobsDisplacement5 = self.mobsDisplacement5 - 2 - a
                    elif self.mobsSpeed == 2 and not self.physics:
                        self.mobsDisplacement1 = self.mobsDisplacement1 - a
                        self.mobsDisplacement2 = self.mobsDisplacement2 - a
                        self.mobsDisplacement3 = self.mobsDisplacement3 - a
                        self.mobsDisplacement4 = self.mobsDisplacement4 - a
                        self.mobsDisplacement5 = self.mobsDisplacement5 - a
            if self.passLevel == 2 and self.difficulty == 2:
                if self.mobsStaticDisplacement == 60:
                    self.mobsDisplacement1 += 55
                    self.mobsDisplacement2 += 55
                    self.mobsDisplacement3 += 55
                    self.mobsDisplacement4 += 55
                    self.mobsDisplacement5 += 55
                    self.mobsStaticDisplacement += 55
                elif self.mobsStaticDisplacement == 114:
                    self.mobsDisplacement1 -= 55
                    self.mobsDisplacement2 -= 55
                    self.mobsDisplacement3 -= 55
                    self.mobsDisplacement4 -= 55
                    self.mobsDisplacement5 -= 55
                    self.mobsStaticDisplacement -= 55

    # ANIMATED BLOCKS

    def LavaAnimation(self):
        if self.passLevel == 1:
            self.lavaAnimationVariable += 0.5
            if self.lavaAnimationVariable % 16 == 0:
                self.lavaAnimation += 1
                if self.lavaAnimation == 16:
                    self.lavaAnimation = 0

    # ASSETS

    def Tree(self, x):
        px.blt(self.x + x, 96, 1, 32, 0, 16, 16)
        px.blt(self.x + x, 80, 1, 32, 0, 16, 16)
        px.blt(self.x + x, 64, 1, 32, 0, 16, 16)
        px.blt(self.x + x - 16, 64, 1, 48, 0, 16, 16, 0)
        px.blt(self.x + x, 64, 1, 48, 0, 16, 16, 0)
        px.blt(self.x + x + 16, 64, 1, 48, 0, 16, 16, 0)
        px.blt(self.x + x - 16, 48, 1, 48, 0, 16, 16, 0)
        px.blt(self.x + x, 48, 1, 48, 0, 16, 16, 0)
        px.blt(self.x + x + 16, 48, 1, 48, 0, 16, 16, 0)
        px.blt(self.x + x, 32, 1, 48, 0, 16, 16, 0)

    def LavaBlock(self, x, y):
        px.blt(self.x + x, y + self.lavaAnimation, 1, 208, 0, 16, 16 - self.lavaAnimation)
        px.blt(self.x + x, y, 1, 208, 16 - self.lavaAnimation, 16, 0 + self.lavaAnimation)

    def Land(self, y, block, depth):
        for i in range(0, 1600):
            if i % 16 == 0:
                if (((i != 608 and i != 624 and i != 640 and i != 656 and i != 688 and i != 704 and
                     i != 720 and i != 736) or self.passLevel != 1) or depth != 8) and ((i != 736 and i != 752 and i != 768 and i != 784 and i != 800) or self.passLevel != 2):
                    px.blt(self.x + i, y, 1, block, 0, 16, depth)

    def NetherPortal(self, x):
        # Obsidian
        px.blt(self.x + x, 96, 1, 112, 0, 16, 16)
        px.blt(self.x + x + 16, 96, 1, 112, 0, 16, 16)
        px.blt(self.x + x + 32, 96, 1, 112, 0, 16, 16)
        px.blt(self.x + x + 48, 96, 1, 112, 0, 16, 16)
        px.blt(self.x + x, 80, 1, 112, 0, 16, 16)
        px.blt(self.x + x + 48, 80, 1, 112, 0, 16, 16)
        px.blt(self.x + x, 64, 1, 112, 0, 16, 16)
        px.blt(self.x + x + 48, 64, 1, 112, 0, 16, 16)
        px.blt(self.x + x, 48, 1, 112, 0, 16, 16)
        px.blt(self.x + x + 48, 48, 1, 112, 0, 16, 16)
        px.blt(self.x + x, 32, 1, 112, 0, 16, 16)
        px.blt(self.x + x + 16, 32, 1, 112, 0, 16, 16)
        px.blt(self.x + x + 32, 32, 1, 112, 0, 16, 16)
        px.blt(self.x + x + 48, 32, 1, 112, 0, 16, 16)
        # Portal
        px.blt(self.x + x + 16, 80, 1, 96, 0, 16, 16)
        px.blt(self.x + x + 32, 80, 1, 96, 0, 16, 16)
        px.blt(self.x + x + 16, 64, 1, 96, 0, 16, 16)
        px.blt(self.x + x + 32, 64, 1, 96, 0, 16, 16)
        px.blt(self.x + x + 16, 48, 1, 96, 0, 16, 16)
        px.blt(self.x + x + 32, 48, 1, 96, 0, 16, 16)

    def Cloud(self):
        cloudX = [28, 72, 137, 201, 286, 313, 353, 454, 536, 580, 625, 662, 700, 776, 841, 896, 944, 1002, 1057, 1109, 1193, 1229, 1524, 1307, 1394, 1443, 1504, 1576]
        cloudY = [26, 16, 36, 21, 6, 36, 11, 6, 26, 31, 6, 36, 6, 26, 6, 21, 1, 21, 1, 16, 16, 1, 26, 11, 6, 31, 11, 1]
        for i in range(0, len(cloudX)):
            px.blt(self.x + cloudX[i], cloudY[i], 1, 160, 0, 16, 16, 0)

    def BricksLevel1(self):
        brickX = [1146, 1162, 1162, 1205, 1248, 1291, 1334, 1378, 1378, 1394]
        brickY = [96, 96, 80, 64, 64, 64, 64, 80, 96, 96]
        for i in range(len(brickX)):
            px.blt(self.x + brickX[i], brickY[i], 1, 176, 0, 16, 16)

    def TopDetailsNether(self):
        netherrackX = [64, 80, 160, 208, 240, 442, 1040, 1360]
        netherrackY = [16, 16, 16, 16, 16, 16, 16, 16]
        glowstoneX = [512, 528, 528, 544, 752, 768, 784, 800, 784, 800, 816, 992, 1008, 1024, 992, 1008, 1392, 1408, 1408]
        glowstoneY = [16, 16, 0, 0, 0, 0, 0, 0, 16, 16, 16, 0, 0, 0, 16, 16, 16, 16, 0]
        for i in range(16, 112):
            if i % 16 == 0:
                self.LavaBlock(224, i)
                self.LavaBlock(442, i)
                self.LavaBlock(1024, i)
                self.LavaBlock(1376, i)
        for i in range(len(netherrackX)):
            px.blt(self.x + netherrackX[i], netherrackY[i], 1, 192, 0, 16, 16)
        for i in range(len(glowstoneX)):
            px.blt(self.x + glowstoneX[i], glowstoneY[i], 1, 224, 0, 16, 16)

    def LavaFloor(self):
        for i in range(608, 752):
            if i % 16 == 0 and i != 672:
                px.blt(self.x + i, 113, 1, 208, 0, 16, 7)

    def EndPortal(self, x):
        for i in range(0, 80):
            if i % 16 == 0:
                px.blt(self.x + x + i, 96, 1, 144, 0, 16, 16, 0)

    def EndProtection(self, x):
        px.blt(self.x + x, 64, 1, 128, 0, 16, 16)
        px.blt(self.x + x + 16, 64, 1, 128, 0, 16, 16)
        px.blt(self.x + x + 32, 64, 1, 128, 0, 16, 16)
        
    def House(self):
        px.blt(self.x + 1520, 96, 1, 16, 0, 16, 16)  # 1o Bloco Baixo
        px.blt(self.x + 1536, 96, 1, 16, 0, 16, 16)  # 2o Bloco Baixo
        px.blt(self.x + 1552, 96, 1, 16, 0, 16, 16)  # 3o Bloco Baixo
        px.blt(self.x + 1568, 96, 1, 16, 0, 16, 16)  # 4o Bloco Baixo
        px.blt(self.x + 1584, 96, 1, 16, 0, 16, 16)  # 5o Bloco Baixo
        px.blt(self.x + 1520, 80, 1, 16, 0, 16, 16)  # 1o Bloco Meio
        px.blt(self.x + 1536, 80, 1, 16, 0, 16, 16)  # 2o Bloco Meio
        px.blt(self.x + 1552, 80, 1, 16, 0, 16, 16)  # 3o Bloco Meio
        px.blt(self.x + 1568, 80, 1, 16, 0, 16, 16)  # 4o Bloco Meio
        px.blt(self.x + 1584, 80, 1, 16, 0, 16, 16)  # 5o Bloco Meio
        px.blt(self.x + 1520, 64, 1, 16, 0, 16, 16)  # 1o Bloco Cima
        px.blt(self.x + 1536, 64, 1, 16, 0, 16, 16)  # 2o Bloco Cima
        px.blt(self.x + 1552, 64, 1, 16, 0, 16, 16)  # 3o Bloco Cima
        px.blt(self.x + 1568, 64, 1, 16, 0, 16, 16)  # 4o Bloco Cima
        px.blt(self.x + 1584, 64, 1, 16, 0, 16, 16)  # 5o Bloco Cima
        px.blt(self.x + 1568, 80, 1, 64, 0, 16, 16, 0)  # Vidro
        px.blt(self.x + 1536, 80, 1, 80, 0, 16, 32, 0)  # Porta


    '#TEXT'

    def DieText(self):
        if not self.alive:
            px.text(81, 10, "Morreu Calvin!", px.frame_count % 16)
            px.text(58, 16, "ESPACO - Tentar Novamente", px.frame_count % 16)
            px.text(73, 22, "Q - Fechar o jogo", px.frame_count % 16)

    '#MOBS'

    def Mobs(self):
        mobsDisplacement = [self.mobsDisplacement1, self.mobsDisplacement2, self.mobsDisplacement3, self.mobsDisplacement4, self.mobsDisplacement5]
        endermanHead = [self.endermanHead1, self.endermanHead2, self.endermanHead3, self.endermanHead4, self.endermanHead5]
        for i in range(0, len(mobsDisplacement)):
            if self.passLevel == 0:
                px.blt(mobsDisplacement[i] + 50, 80, 2, self.mobsAnimation, 0, 14, 32, 0)
            elif self.passLevel == 1:
                px.blt(mobsDisplacement[i] + 50, 80, 2, self.mobsAnimation, 128, 16, 32, 5)
            elif self.passLevel == 2:
                px.blt(mobsDisplacement[i] + 50, 73, 2, self.mobsAnimation, 32 if self.mobsWay == 0 else 71, 26, 39, 5)
                px.blt(mobsDisplacement[i] + 59, 65 if endermanHead[i] == 0 else 64, 2, 56 if self.mobsWay == 0 else 48, endermanHead[i], 8, 8 if endermanHead[i] == 0 else 10, 5)
                
    '#DRAW'

    def Draw(self):
        # Menu Screen
        if not self.start:
            self.MenuScreen()
        elif self.start:
            # Level 1 - Overworld
            if self.passLevel == 0:
                px.cls(12)
                if not self.alive:
                    px.cls(0)
                self.Die()
                self.NetherPortal(1520)
                self.BricksLevel1()
                px.blt(self.playerX, self.playerY, 0, self.playerAnimation, self.playerWay, 21, self.playerOnFire, 0)
                self.Land(112, 0, 8)
                self.Cloud()
                self.Tree(248)
                self.Tree(416)
                self.Tree(744)
                self.Tree(928)
                self.Mobs()
                self.DieText()
                self.PauseScreen()
            # Level 2 - Nether
            elif self.passLevel == 1:
                px.cls(8)
                if not self.alive:
                    px.cls(0)
                self.Die()
                self.NetherPortal(16)
                self.EndPortal(1504)
                px.blt(self.playerX, self.playerY, 0, self.playerAnimation, self.playerWay, 21, self.playerOnFire, 0)
                self.Land(112, 192, 8)
                self.Land(0, 192, 16)
                self.LavaFloor()
                self.TopDetailsNether()
                self.Mobs()
                self.DieText()
                self.PauseScreen()
            # Level 3 - End
            elif self.passLevel == 2:
                px.cls(1)
                if not self.alive:
                    px.cls(0)
                self.Die()
                self.EndPortal(1504)
                self.EndProtection(208)
                self.EndProtection(362)
                self.EndProtection(535)
                self.EndProtection(1054)
                self.EndProtection(1330)
                px.blt(self.x + 704, 96, 1, 128, 0, 16, 16)
                px.blt(self.x + 720, 96, 1, 128, 0, 16, 16)
                px.blt(self.x + 720, 80, 1, 128, 0, 16, 16)
                px.blt(self.playerX, self.playerY, 0, self.playerAnimation, self.playerWay, 21, self.playerOnFire, 0)
                self.Mobs()
                self.Land(112, 128, 8)
                px.blt(self.x + 16, 112, 1, 112, 0, 16, 8)
                px.blt(self.x + 32, 112, 1, 112, 0, 16, 8)
                px.blt(self.x + 48, 112, 1, 112, 0, 16, 8)
                px.blt(self.x + 64, 112, 1, 112, 0, 16, 8)
                self.DieText()
                self.PauseScreen()
            # Level 4 - Overworld
            elif self.passLevel == 3:
                px.cls(12)
                if not self.alive:
                    px.cls(0)
                self.Die()
                self.House()
                self.Land(112, 0, 8)
                self.Cloud()
                self.Tree(248)
                self.Tree(416)
                self.Tree(744)
                self.Tree(928)
                px.blt(self.playerX, self.playerY, 0, self.playerAnimation, self.playerWay, 21, self.playerOnFire, 0)
                self.DieText()
                self.PauseScreen()
            elif self.passLevel == 4:
                self.Victory()


SuperCalvinBros()
