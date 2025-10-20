from app import main

def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert "CI/CD" in captured.out
