"""
채점 스크립트

아래 SOLUTION에 채점할 파일을 "폴더/파일.py" 형식으로 입력하고 실행한다.
    예) "2/1.py" → Answer의 섹션 2 / 1번 문제의 in*.txt, out*.txt 로 채점
"""

import os
import re
import subprocess
import sys
import tempfile
import time

SOLUTION = "6/4.py"  # ← 여기에 직접 입력
TIME_LIMIT = 1  # 초

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ANSWER_DIR = os.path.normpath(os.path.join(BASE_DIR, "../../Answer/pythonalgorithm_formac"))


def find_problem_dir():
    section, file = os.path.split(SOLUTION)
    problem = re.match(r"\d+", file).group(0)
    section_dir = os.path.join(ANSWER_DIR, f"섹션 {section}")
    for name in os.listdir(section_dir):
        # "1. k번째 약수", "1, 2. 네트워크 선 자르기" 같은 형식 지원
        m = re.match(r"([\d,\s]+)\.", name)
        if m and problem in re.findall(r"\d+", m.group(1)):
            return os.path.join(section_dir, name)
    sys.exit(f"섹션 {section}에서 {problem}번 문제 폴더를 찾지 못했습니다.")


def decode(raw):
    # 일부 정답 파일은 BOM이 붙은 UTF-16이라 BOM을 보고 인코딩을 고른다
    if raw.startswith((b"\xff\xfe", b"\xfe\xff")):
        return raw.decode("utf-16")
    return raw.decode("utf-8-sig", errors="replace")


def normalize(text):
    # 줄 끝 공백, 빈 줄 차이는 무시
    return [" ".join(line.split()) for line in text.strip().splitlines() if line.strip()]


def run(solution, in_path):
    with tempfile.TemporaryDirectory() as tmp:
        # 풀이 안의 open("input.txt")가 그대로 동작하도록 input.txt로 복사
        # 테스트 파일이 윈도우 줄바꿈(\r\n)이라 input()에 \r이 붙지 않도록 변환
        tmp_input = os.path.join(tmp, "input.txt")
        with open(in_path, "rb") as f:
            data = f.read().replace(b"\r\n", b"\n")
        with open(tmp_input, "wb") as f:
            f.write(data)

        start = time.perf_counter()
        try:
            proc = subprocess.run(
                [sys.executable, solution], cwd=tmp, input=data,
                capture_output=True, timeout=TIME_LIMIT,
            )
        except subprocess.TimeoutExpired:
            return "시간 초과", time.perf_counter() - start, ""
        elapsed = time.perf_counter() - start
        if proc.returncode:
            return "런타임 에러", elapsed, ""
        return None, elapsed, proc.stdout.decode("utf-8", errors="replace")


def main():
    solution = os.path.join(BASE_DIR, SOLUTION)
    problem_dir = find_problem_dir()
    cases = sorted(int(m.group(1)) for f in os.listdir(problem_dir) if (m := re.fullmatch(r"in(\d+)\.txt", f)))
    print(f"[{os.path.basename(problem_dir)}] 제한 시간 {TIME_LIMIT}초\n")

    passed = 0
    for n in cases:
        error, elapsed, out = run(solution, os.path.join(problem_dir, f"in{n}.txt"))
        if error is None:
            with open(os.path.join(problem_dir, f"out{n}.txt"), "rb") as f:
                expected = decode(f.read())
            error = None if normalize(out) == normalize(expected) else "오답"

        if error is None:
            passed += 1
            print(f"✅ 테스트 {n}: 정답 ({elapsed * 1000:.0f}ms)")
        else:
            print(f"❌ 테스트 {n}: {error} ({elapsed * 1000:.0f}ms)")

    print(f"\n결과: {passed}/{len(cases)} 통과")


if __name__ == "__main__":
    main()
