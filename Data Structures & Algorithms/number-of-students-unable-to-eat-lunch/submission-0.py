class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int: 
        queue = deque(students)
        sandwich_index = 0
        rotations = 0

        while queue and rotations < len(queue):
            if queue[0] == sandwiches[sandwich_index]:
                queue.popleft()
                sandwich_index += 1
                rotations = 0
            else:
                student = queue.popleft()
                queue.append(student)
                rotations += 1
        return len(queue)
