import typing as t


class Frame:
    def __init__(self, frame_num: int):
        self.frame_num: int = frame_num
        self.rolls: t.List[int] = []
        self.raw_score: int = 0
        self.bonus_score: int = 0
        self.bonus_balls: int = 0
        self.done: bool = False

    def score(self) -> int:
        return self.raw_score + self.bonus_score

    def is_spare(self) -> bool:
        return not self.is_strike() and self.raw_score == 10

    def is_strike(self) -> bool:
        return self.rolls and self.rolls[0] == 10
    
    def add_roll(self, pins: int):
        self.rolls.append(pins)
        self.raw_score += pins

        if len(self.rolls) == 1:
            if self.is_strike():
                self.bonus_balls = 2
                self.done = True
        
        else:
            self.done = True
            if self.is_spare():
                self.bonus_balls = 1

    def add_bonus_roll(self, pins: int):
        self.bonus_score += pins
        self.bonus_balls -= 1

    def get_roll_score(self) -> int:
        while True:
            
            frame_max = 10 - self.raw_score if self.frame_num < 10 else 10
            ball_num = len(self.rolls) + 1
            score = input(f"Ball {ball_num}: pins knocked?: ")
            try:
                score = int(score)
                if score > frame_max or score < 0:
                    raise Exception
                return score

            except:
                print(f"Must be a valid score between 0 and {frame_max}")


class Game:
    def __init__(self):
        self.frames: t.List[Frame] = [Frame(i) for i in range(1, 11)]
        self.incomplete_frames = set()

    def start_bowling(self):
        for frame in self.frames:
            print(f"\nBowling Frame {frame.frame_num} | Current Score: {self.current_score()}")
            self._bowl_frame(frame)

        print(f"\nFINAL SCORE: *{self.current_score()}*\n")

    def _bowl_frame(self, frame):
        while not frame.done:
            pins = frame.get_roll_score()
            frame.add_roll(pins)
            self._add_bonus_to_prev_frames(pins)
        
        if frame.frame_num == 10 and frame.bonus_balls:
            while frame.bonus_balls:
                pins = frame.get_roll_score()
                frame.add_bonus_roll(pins)
                self._add_bonus_to_prev_frames(pins)
        else:
            if frame.bonus_balls:
                self.incomplete_frames.add(frame)

    def _add_bonus_to_prev_frames(self, pins: int):
        completed = []
        for frame in self.incomplete_frames:
            frame.add_bonus_roll(pins)

            if not frame.bonus_balls:
                completed.append(frame)
            
        for frame in completed:
            self.incomplete_frames.remove(frame)

    def current_score(self):
        return sum([f.score() for f in self.frames])


# game = Game()
# game.start_bowling()
