'''
Container with calendar data

John Oldman    October 2017

'''




class CalData:
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
        self._build_birthdays()
        self._build_aniversaries()
        self._build_appointment()
    def _build_birthdays(self):
        '''
        Method:         _build_birthdays
        Parameters:     None
        Returns:        None
        Description:    builds the birthdays for a year.
        '''
        self._birthdays.append({'month':'1' , 'day':'14', 'name':'Test'  , 'year':1985})
    def _build_aniversaries(self):
        '''
        Method:         _build_aniversaries
        Parameters:     None
        Returns:        None
        Description:    builds the aniversaries for a year.
        '''
        self._aniversaries.append({'month':'1' , 'day':'27', 'name':'test'            , 'year':2014})
    def _build_appointment(self):
        '''
        Method:         _build_appointment
        Parameters:     None
        Returns:        None
        Description:    builds the appointments for a year.
        '''
        self._appointments.append({'month':'1' , 'day':'2' , 'name':'Test'})
    def get_birthdays(self):
        ''' getter '''
        return self._birthdays
    def get_aniversaries(self):
        ''' getter '''
        return self._aniversaries
    def get_appointments(self):
        ''' getter '''
        return self._appointments

