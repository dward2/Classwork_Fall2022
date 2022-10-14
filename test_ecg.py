def test_add_plot():
    from ecg import add_plot
    answer = add_plot(4)
    assert answer == 9
