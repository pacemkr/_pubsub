=========
PySignalsEx
=========
PySignalsEx is a signal dispatcher for Python, extracted from the Django framework, and extended to provide a special "capture all" signal called any_signal. This special signal is useful for instrumentation, logging, auditing, debugging, etc.

For a version that is true to Django, without this extension, see https://github.com/theojulienne/PySignals

Example
=====
PySignalsEx is originally extracted from the Django framework, therefore the best
place to get documentation is from the `Django Signals Documentation <http://docs.djangoproject.com/en/dev/topics/signals/>`_.

Additionally, PySignalsEx provides a special signal called 'any_signal'. When you listen for this signal, your listener will be notified of all signals sent in your application. You listen for any_signal as you would for any other.

::

        from pysignalsex import Signal, receiver, any_signal

        @receiver(any_signal)
        def mylistener(sender, **kwargs):
                print "kwargs:", kwargs
                if kwargs['signal'] == mysignal:
                        print "mysignal"
                if kwargs['signal'] == myothersignal:
                        print "myothersignal"

        mysignal = Signal(providing_args=['myarg'])
        myothersignal = Signal()

        mysignal.send(sender='sender1', myarg='myval')
        myothersignal.send(sender='sender2')
