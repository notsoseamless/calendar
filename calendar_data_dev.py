'''
Container with calendar data

notsoseamless -October 2017

'''




class CalData(object):
    ''' represents calenda data '''
    def __init__(self):
        '''
        Method:         __init__
        Parameters:     None
        Returns:        None
        Description:    Initialise all variables.
        '''
        self._birthdays = []
        self._aniversaries = []
        self._appointments = []
        self._bank_days = []
        self._build_birthdays()
        self._build_aniversaries()
        self._build_appointment()
        self._build_bank_holidays()
    def _build_birthdays(self):
        '''
        Method:         _build_birthdays
        Parameters:     None
        Returns:        None
        Description:    builds the birthdays for a year.
        '''
        self._birthdays.append({'month':'1', 'day':'14', 'name':'Test' , 'year':1985})
        self._birthdays.append({'month':'1', 'day':'24', 'name':'Test' , 'year':1900})
    def _build_aniversaries(self):
        '''
        Method:         _build_aniversaries
        Parameters:     None
        Returns:        None
        Description:    builds the aniversaries for a year.
        '''
        self._aniversaries.append({'month':'1', 'day':'27', 'name':'test', 'year':2014})
        self._aniversaries.append({'month':'1', 'day':'20', 'name':'test', 'year':0})
    def _build_appointment(self):
        '''
        Method:         _build_appointment
        Parameters:     None
        Returns:        None
        Description:    builds the appointments for a year.
        '''
        self._appointments.append({'month':'1', 'day':'2', 'name':'Test', 'year':0})

    def _build_bank_holidays(self):
        '''
        Method:         _build_bank_holidayss
        Parameters:     None
        Returns:        None
        Description:    builds the bank holidays for a year.
        '''
        self._bank_days.append({'month':'1'  , 'day':'1' , 'name':'NEW YEAR'  , 'year':0})
        self._bank_days.append({'month':'8'  , 'day':'28', 'name':'SUMMER BH' , 'year':0})
        self._bank_days.append({'month':'12' , 'day':'25', 'name':'XMAS'      , 'year':0})
        self._bank_days.append({'month':'12' , 'day':'26', 'name':'BOXING DAY', 'year':0})

    @property
    def birthdays(self):
        return self._birthdays

    @property
    def aniversaries(self):
        return self._aniversaries

    @property
    def appointments(self):
        return self._appointments

    @property
    def bank_days(self):
        return self._bank_days

