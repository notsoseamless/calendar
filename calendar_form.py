'''
Script to generate a calendar
'''



import calendar
from reportlab.lib import colors
from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4, inch, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle 
from calendar_data import CalData
 

# constants
CALENDER_FILE     = "calendar_form.pdf"
YEAR              = 2018
FIRST_DAY_OF_WEEK = calendar.MONDAY # for calendar class.
START_DAY         = 0 #Calendar starting day, default of 0 means Monday, 2 Tuesday, etc
MONTHS            = ['blank', 'January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Decemeber']



def main():
    ''' the main function '''
    first_day_of_week = START_DAY # Monday
    data = CalendarData()
    month = 4

    for month in range(1,13):
        CalendarGrid(YEAR, month, data, first_day_of_week) 

    
class CalendarGrid(object):
    '''
    Class:          CalendarGrid
    Description:    represents a month
    Requirements:   None
    '''
    def __init__(self, year, month, data, first_day_of_week=0):
        '''
        Method:         __init__
        Parameters:     year as integer
                        month as integer
                        first_day_of_week, zero = Monday
                        data class instant
        Returns:        None
        Description:    Initialise all variables.
                        Invokes the Table instant
        '''
        # local variables
        self._first_day_of_week = first_day_of_week
        self._data = data
        self._year = year
        self._month = month
        self._elements = []
        out_file = 'Calendar_' + MONTHS[self._month] + '_' + str(year) + '.pdf'
        self._doc = SimpleDocTemplate(out_file, pagesize=landscape(A4), rightMargin=0, leftMargin=0, topMargin=20, bottomMargin=0)
        # invoke calender class calc
        self.cal = calendar
        self.cal.setfirstweekday(FIRST_DAY_OF_WEEK)
        self._week_data = None
        self._week = None
        self._title = None
        self.make_month()

    def _make_title(self):
        '''
        Method:         _make_title
        Parameters:     None
        Returns:        None
        Description:    Sets up the month name followed by the year.
        '''
        title_str = MONTHS[self._month] + ' ' + str(self._year)
        self._title=Table([[title_str]], 1*[5*inch], 1*[0.5*inch])
        self._title.setStyle(TableStyle([('ALIGN',    (0,0), (0,0), 'CENTRE'),
                                         ('VALIGN',   (0,0), (0,0), 'TOP'),
                                         ('TEXTCOLOR',(0,0), (0,0), colors.blue),
                                         ('BOX',      (0,0), (0,0), 0.25, colors.white),
                                         ('VALIGN',   (0,0), (0,0), 'TOP'),
                                         ('FONTSIZE', (0,0), (0,0), 25),
                                        ]))

    def _make_day_headers(self, first_day=0):
        '''
        Method:         _make_day_headers
        Parameters:     Calendar week start day, defaults to Monday.
        Returns:        None
        Description:    Sets up the first row of the month table with the day names
                        depending on the first day of the week.
        '''
        day_set = ['Monday', 'Tuesday', 'Wedensday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        # set up days depending on first day of the week, zero being monday.
        days_in_week = 7
        day_pointer  = first_day
        days = [[day_set[(day_pointer + day_of_week) % days_in_week] for day_of_week in range(days_in_week)]]
        # set up the day header table
        self._week = Table(days,7*[1.5*inch], 1*[0.25*inch])
        self._week.setStyle(TableStyle([('ALIGN' ,     (0,0), (-1,-1), 'CENTRE'),
                                        ('VALIGN',     (0,0), (-1,-1), 'MIDDLE'),
                                        ('INNERGRID',  (0,0), (-1,-1), 0.25, colors.blue),
                                        ('BACKGROUND', (0,0), (-1,-1), colors.blue),
                                        ('BOX',        (0,0), (-1,-1), 0.25, colors.blue),
                                        ('TEXTCOLOR',  (0,0), (-1,-1), colors.white),
                                        ('FONTSIZE',   (0,0), (-1,-1), 14),
                                       ]))

        
    def _make_data(self):
        '''
        Method:         _make_data
        Parameters:     None
        Returns:        None
        Description:    produce data for each day of the month, if it exists.
        '''
        blank_days = calendar.monthrange(self._year, self._month)[0]
        days_in_month = calendar.monthrange(self._year, self._month)[1]
        days_in_week  = 7
        date  = - blank_days
        if days_in_month + blank_days > (days_in_week * 5):
	        weeks_in_month = 6
        else:
            weeks_in_month = 5

        data = []
        data.append(self._build_week(date))
        data.append(self._build_week(date + days_in_week))
        data.append(self._build_week(date + days_in_week * 2))
        data.append(self._build_week(date + days_in_week * 3))
        data.append(self._build_week(date + days_in_week * 4))

        if 6 == weeks_in_month:
            data.append(self._build_week(date + days_in_week * 5))
        # output to table 
        self._week_data=Table(data,7*[1.5*inch], weeks_in_month*[1.0*inch])
        self._week_data.setStyle(TableStyle([('ALIGN' ,     (0,0), (-1,-1), 'RIGHT'),
                                             ('VALIGN',     (0,0), (-1,-1), 'TOP'),
                                             ('INNERGRID',  (0,0), (-1,-1), 0.25, colors.blue),
                                             ('BACKGROUND', (5,0), (-1,-1), colors.lavender),
                                             ('TEXTCOLOR',  (0,0), (-1,-1), colors.blue),
                                             ('BOX',        (0,0), (-1,-1), 0.25, colors.blue),
                                             ('FONTSIZE',   (0,0), (-1,-1), 13),
                                            ]))
    def _build_week(self, date):
        ''' 
        Method:         _build_week
        Parameters:     data - date of first week day
        Returns:        list of week
        Description:   
        '''
        days_in_week  = 7
        days_in_month = calendar.monthrange(self._year, self._month)[1]
        week = []
        for day_in_week in range(days_in_week):
            if date < days_in_month:
                date = date + 1
                if date > 0:
                    day_data = self._data.get(self._month, date)
                    day_data_str =  '[%s]' % ', '.join(map(str, day_data))
                    week.append(str(date) + '\n' + day_data_str.strip('[],'))
                else:
                    week.append('')
            else:
                week.append('')
        return week 
    def make_month(self):
        '''
        Method:         make_month
        Parameters:     None
        Returns:        None
        Description:    Produces the completed grid for a month.
        '''
        self._make_title()
        self._make_day_headers(self._first_day_of_week)
        self._make_data()
        self._elements.append(self._title)
        self._elements.append(self._week)
        self._elements.append(self._week_data)
        self._doc.build(self._elements)


class CalendarData(object):
    '''
    Class:          CalendarData
    Description:    Represents calendar data container
    Requirements:   None
    '''
    def __init__(self):
        '''
        Method:         __init__
        Parameters:     None
        Returns:        None
        Description:    Initialise all variables.
        '''
        # import data from cal_data
        # instanciate CalData object and import date data
        cal_data = CalData()
        self._birthdays    = cal_data.birthdays
        self._aniversaries = cal_data.aniversaries
        self._appointments = cal_data.appointments
        self._bank_days    = cal_data.bank_days
    def get(self, month, day):
        '''
        Method:         get
        Parameters:     Month and day
        Returns:        The compiled data.
        Description:    getter compiles birthdays, anivarsaries and appointments for a given month-day.
        '''
        results =  self._sort_date_lists(month, day, self._bank_days)
        results += self._sort_date_lists(month, day, self._birthdays)
        results += self._sort_date_lists(month, day, self._aniversaries)
        results += self._sort_date_lists(month, day, self._appointments)
        return results

    def _sort_date_lists(self, month, day, list_to_sort):
        '''
        Method:         sort_date_lists
        Parameters:     Month and day
        Returns:        The compiled data.
        Description:    gets month then day data from list_to_sort.
        '''
        years = lambda Yr : ' (' + str(YEAR - Yr) + ')\n' if Yr > 0  else '\n'
        month_list = filter(lambda month_list: str(month) == month_list['month'], list_to_sort)
        day_list =   filter(lambda day_list: str(day) == day_list['day'], month_list)
        return [data['name'] + years(data['year']) + '\n' for data in day_list]



if __name__ == '__main__':
    main()
    print "PDF created!"

