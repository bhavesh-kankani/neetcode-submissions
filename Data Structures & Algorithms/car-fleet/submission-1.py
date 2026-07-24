class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        kinematics = sorted(zip(position, speed), reverse=True)
        for position, speed in kinematics:
            distance = (target-position)
            time = distance/speed
            if stack and time < stack[-1]:
                stack.append(stack[-1])
            else:
                stack.append(time)
        return len(set(stack))