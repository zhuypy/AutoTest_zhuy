import time
import eventlet

def sleep(sleepTime,unit=1):
    '''
    等待，默认单位为秒，传入unit翻倍
    waiting
    :param sleepTime: specify waiting time
    :return:None
    '''
    time.sleep(sleepTime*unit)

def getCurrentTime():
    '''
    获取当前时间，格式为  年_月_日_时_分_秒
    get current time
    :return: Y_m_d_H_M_S
    '''
    return time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime())

def getCurrentDate():
    '''
    获取当前时间，格式为 年_月_日
    get current date
    :return: Y_m_d
    '''
    return time.strftime('%Y_%m_%d',time.localtime())

def timeMeter(fun):
    '''
    计时器，计算函数执行时间，装饰器调用
    :param fun:
    :return:
    '''
    def timeMeter_inner(*args,**kwargs):
        time_start = time.localtime()
        print('start time is %s'%(time.strftime('%Y_%m_%d_%H_%M_%S',time_start)))
        fun(*args,**kwargs)
        time_end = time.localtime()
        print('start time is %s'%(time.strftime('%Y_%m_%d_%H_%M_%S',time_end)))
        print('time consuming : %s'%(time.mktime(time_end)-time.mktime(time_start)))
        return fun
    return timeMeter_inner

def timer(timeout):
    '''
    超时器，函数执行时间超时，则抛出异常并阻断执行【未完成的函数】
    :param timeout:
    :return:
    '''
    def timer_outer(fun):
        def timer_inner(*args,**kwargs):
            fun(*args,**kwargs)
        return timer_inner
    return timer_outer











