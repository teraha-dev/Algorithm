def solution(citations, M = 0): return len([(M := M + 1) for i in sorted(citations, reverse=True) if i > M])