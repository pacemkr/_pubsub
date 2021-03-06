import py
from pubsub import Signal, receiver, any_signal

def test_any_signal_listener():
    outputall = []
    output1 = []
    output2 = []

    @receiver(any_signal)
    def listenerall(sender, **named):
        outputall.append(named)

    some_signal1 = Signal()
    @receiver(some_signal1)
    def listener1(sender, **named):
        output1.append(named)

    some_signal2 = Signal(providing_args=['arg1', 'arg2'])
    @receiver(some_signal2)
    def listener2(sender, **named):
        output2.append(named)

    some_signal1.send('test')
    some_signal2.send('test', arg1='val1', arg2='val2')
    some_signal1.send('test')

    print "output1 =>", output1
    print "output2 =>", output2
    print "outputall =>", outputall

    assert len(output1) == 2
    assert output1[0]['signal'] == some_signal1
    assert len(output2) == 1
    assert output2[0]['signal'] == some_signal2
    assert output2[0]['arg1'] == 'val1'
    assert output2[0]['arg2'] == 'val2'

    assert len(outputall) == 3
    assert outputall[0]['signal'] == some_signal1
    assert outputall[1]['signal'] == some_signal2
    assert outputall[2]['signal'] == some_signal1
    assert len(outputall[0]) == 1
    assert outputall[1]['arg1'] == 'val1'
    assert outputall[1]['arg2'] == 'val2'
    assert len(outputall[2]) == 1


def test_call_method():
    signal = Signal(providing_args=['truthiness'])

    @receiver(signal)
    def foo(sender, **named):
        return 'kindatrue' if named['truthiness'] else 'false'

    assert signal.call(sender='test', truthiness=True) == 'kindatrue'
    assert signal.call(sender='test', truthiness=False) == 'false'

def test_default_sender():
    signal = Signal()

    @receiver(signal)
    def check_sender(sender, **named):
        print sender
        assert sender == 'tests.test_signals test_default_sender'

    signal.send()
    signal.call()
    signal.send_robust()


def test_default_sender_from_class():
    signal = Signal()

    @receiver(signal)
    def check_sender(sender, **named):
        print sender
        assert sender == 'tests.test_signals my_closure'

    def my_closure():
        signal.send()

    my_closure()
