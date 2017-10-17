

#import pyPdf
import time
import datetime as dt
import calendar
import re
import StringIO
from reportlab.lib import colors
from reportlab.lib import utils
from reportlab.lib.pagesizes import landscape, A4
from reportlab.platypus import (Image, SimpleDocTemplate, Paragraph, Spacer)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch, mm
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, inch, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from calendar_data import CalData
 

# constants
CALENDER_FILE     = "calendar_form.pdf"
YEAR              = 2017
FIRST_DAY_OF_WEEK = calendar.MONDAY # for calendar class.
START_DAY         = 0 #Calendar starting day, default of 0 means Mondau, 2 for Tuesday, etc
MONTHS            = ['blank', 'January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Decemeber']



def main():
    ''' the main function '''
    first_day_of_week = START_DAY # Monday
    data = calendar_data()
    month = 1

    # invoke month class
    jan = calendar_grid(YEAR, month, data, first_day_of_week) 
    jan()
    
class calendar_grid:
    '''
    Class:          calendar_grid
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
        self._doc = SimpleDocTemplate(CALENDER_FILE, pagesize=landscape(A4), rightMargin=0, leftMargin=0, topMargin=0, bottomMargin=0)
        # invoke calender class calc
        self.cal = calendar
        self.cal.setfirstweekday(FIRST_DAY_OF_WEEK)
    def __call__(self):
        ''' call method '''
        self.make_month()
    def _make_title(self):
        '''
        Method:         _make_title
        Parameters:     None
        Returns:        None
        Description:    Sets up the month name followed by the year.
        '''
        self._title=Table([[MONTHS[self._month] + ' ' + str(self._year)]])
        self._title.setStyle(TableStyle([('ALIGN',  (0,0), (0,0), 'CENTRE'),
                                         ('VALIGN', (0,0), (0,0), 'BOTTOM'),]))
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
        self._week = Table(days,7*[1.2*inch], 1*[0.25*inch])
        self._week.setStyle(TableStyle([('ALIGN' ,(0,0),(-1,-1), 'CENTRE'),
                                        ('VALIGN',(0,0),(-1,-1), 'MIDDLE'),
                                        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                                        ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                                        ('FONTSIZE', (0,0),(-1,-1), 10),
                                       ]))
    def _make_data(self):
        '''
        Method:         _make_data
        Parameters:     None
        Returns:        None
        Description:    produce data for each day of the month, if it exists.
        '''
        blank_days = calendar.monthrange(self._year, self._month)[0]
        days_in_week  = 7
        date  = - blank_days
        data = []
        data.append(self._build_week(date))
        data.append(self._build_week(date + days_in_week))
        data.append(self._build_week(date + days_in_week * 2))
        data.append(self._build_week(date + days_in_week * 3))
        data.append(self._build_week(date + days_in_week * 4))
        data.append(self._build_week(date + days_in_week * 5))
        # output to table 
        self._week_data=Table(data,7*[1.2*inch], 6*[1.2*inch])
        self._week_data.setStyle(TableStyle([('ALIGN' ,(0,0),(-1,-1),'RIGHT'),
                                             ('VALIGN',(0,0),(-1,-1),'TOP'),
                                             ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                                             ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                                             ('FONTSIZE', (0,0),(-1,-1), 8),
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


class calendar_data:
    '''
    Class:          calendar_data
    Description:    Represents calendar data container
    Requirements:   None
    '''
    '''  '''
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
        self._birthdays = cal_data.get_birthdays()
        self._aniversaries = cal_data.get_aniversaries()
        self._appointments = cal_data.get_appointments()
    def get(self, month, day):
        '''
        Method:         get
        Parameters:     Month and day
        Returns:        The compiled data.
        Description:    getter compiles birthdays, anivarsaries and appointments for a given month-day.
        '''
        results = []
        # birthdays:
        month_list = filter(lambda month_list: str(month) == month_list['month'], self._birthdays)
        day_list =   filter(lambda day_list: str(day) == day_list['day'], month_list)
        for people in day_list:
            results.append('B:' + people['name'] + ' (' +  str(YEAR - people['year']) + ')\n')
        # aniversaries:
        month_list = filter(lambda month_list: str(month) == month_list['month'], self._aniversaries)
        day_list =   filter(lambda day_list: str(day) == day_list['day'], month_list)
        for people in day_list:
            results.append('A:' + people['name'] + ' (' +  str(YEAR - people['year']) + ')\n')
        # appointments
        month_list = filter(lambda month_list: str(month) == month_list['month'], self._appointments)
        day_list =   filter(lambda day_list: str(day) == day_list['day'], month_list)
        for people in day_list:
            results.append(people['name'] + '\n')
        return results


if __name__ == '__main__':
    main()
    print "PDF created!"

