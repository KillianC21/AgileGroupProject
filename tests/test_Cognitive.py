import builtinsgit
from Questionaires.CognitiveEmotionalAssessment import cognitive_emotional_assessment


def test_cognitive_emotional_assessment(monkeypatch):
    # Mock a sequence of valid user inputs (1–10)
    inputs = iter(["8", "7", "9", "6", "8"])

    # Replace input() with our iterator
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    # Run the function being tested
    scores = cognitive_emotional_assessment()

    # Verify we get correct output list
    assert scores == [8, 7, 9, 6, 8]
    assert all(1 <= s <= 10 for s in scores)
