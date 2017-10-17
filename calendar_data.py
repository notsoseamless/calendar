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
        self._birthdays.append({'month':'1' , 'day':'14', 'name':'Test'  , 'year':1986})
        self._birthdays.append({'month':'4' , 'day':'14', 'name':'Mark'  , 'year':1985})
        self._birthdays.append({'month':'4' , 'day':'28', 'name':'Sue'   , 'year':1956})
        self._birthdays.append({'month':'4' , 'day':'28', 'name':'Mia'   , 'year':2010})
        self._birthdays.append({'month':'8' , 'day':'12', 'name':'John'  , 'year':1954})
        self._birthdays.append({'month':'8' , 'day':'20', 'name':'Janet' , 'year':1958})
        self._birthdays.append({'month':'8' , 'day':'20', 'name':'Dave'  , 'year':1958})
        self._birthdays.append({'month':'9' , 'day':'26', 'name':'Mum'   , 'year':1926})
        self._birthdays.append({'month':'10', 'day':'29', 'name':'Lin'   , 'year':1947})
        self._birthdays.append({'month':'12', 'day':'11', 'name':'Freya' , 'year':2013})
        self._birthdays.append({'month':'12', 'day':'14', 'name':'James' , 'year':1987})
    def _build_aniversaries(self):
        '''
        Method:         _build_aniversaries
        Parameters:     None
        Returns:        None
        Description:    builds the aniversaries for a year.
        '''
        self._aniversaries.append({'month':'1' , 'day':'27', 'name':'Z&X'            , 'year':2014})
        self._aniversaries.append({'month':'1' , 'day':'27', 'name':'Z&X'            , 'year':2014})
        self._aniversaries.append({'month':'7' , 'day':'27', 'name':'Mark & Mirel'   , 'year':2014})
        self._aniversaries.append({'month':'8' , 'day':'18', 'name':'Janet & Dave'   , 'year':1987})
        self._aniversaries.append({'month':'8' , 'day':'18', 'name':'Janet'          , 'year':1987})
        self._aniversaries.append({'month':'9' , 'day':'26', 'name':'Dean & Same'    , 'year':2015})
    def _build_appointment(self):
        '''
        Method:         _build_appointment
        Parameters:     None
        Returns:        None
        Description:    builds the appointments for a year.
        '''
        self._appointments.append({'month':'1' , 'day':'2' , 'name':'Testley'})
        self._appointments.append({'month':'1' , 'day':'14', 'name':'TEST_TE'})
        self._appointments.append({'month':'1' , 'day':'14', 'name':'TEST_TE_1'})
        self._appointments.append({'month':'9' , 'day':'2' , 'name':'Audax Ugley'})
        self._appointments.append({'month':'9' , 'day':'6' , 'name':'Lin Spain'})
        self._appointments.append({'month':'9' , 'day':'15', 'name':'Lin Home'})
        self._appointments.append({'month':'9' , 'day':'30', 'name':'Honda Insurance'})
        self._appointments.append({'month':'10', 'day':'7' , 'name':'Audax GtDunmow'})
        self._appointments.append({'month':'10', 'day':'9' , 'name':'John dentist 17:30'})
        self._appointments.append({'month':'11', 'day':'3' , 'name':'Hong Kong'})
        self._appointments.append({'month':'12', 'day':'1' , 'name':'Home'})
    def get_birthdays(self):
        ''' getter '''
        return self._birthdays
    def get_aniversaries(self):
        ''' getter '''
        return self._aniversaries
    def get_appointments(self):
        ''' getter '''
        return self._appointments

