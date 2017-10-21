'''
Script to generate a calendar
'''



import calendar
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, inch, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from calendar_dataP import CalData


# constants
YEAR = 2018
DAYS_IN_WEEK = 7
START_DAY = 0 #Calendar starting day, default of 0 means Monday, 2 Tuesday, etc
MONTHS = ['blank', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Decemeber']



def main():
    ''' the main function '''
    for month in range(1, 13):
        out_file = 'Calendar_' + MONTHS[month] + '_' + str(YEAR) + '.pdf'
        doc = SimpleDocTemplate(out_file, pagesize=landscape(A4), rightMargin=0, leftMargin=0, topMargin=20, bottomMargin=0)
        make_month(month, doc)



def make_month(month, doc):
    '''
    Method:         make_month
    Parameters:     None
    Returns:        None
    Description:    Produces the completed grid for a month.
    '''
    elements = []
    elements.append(make_title(month))
    elements.append(make_day_headers())
    elements.append(make_data(month))
    doc.build(elements)


def make_title(month):
    '''
    Method:         make_title
    Parameters:     None
    Returns:        None
    Description:    Sets up the month name followed by the year.
    '''
    title_str = MONTHS[month] + ' ' + str(YEAR)
    title = Table([[title_str]], 1*[5*inch], 1*[0.5*inch])
    title.setStyle(TableStyle([('ALIGN', (0, 0), (0, 0), 'CENTRE'),
                               ('VALIGN', (0, 0), (0, 0), 'TOP'),
                               ('TEXTCOLOR', (0, 0), (0, 0), colors.blue),
                               ('BOX', (0, 0), (0, 0), 0.25, colors.white),
                               ('VALIGN', (0, 0), (0, 0), 'TOP'),
                               ('FONTSIZE', (0, 0), (0, 0), 25),
                              ]))
    return title


def make_day_headers(first_day=0):
    '''
    Method:         _make_day_headers
    Parameters:     Calendar week start day, defaults to Monday.
    Returns:        None
    Description:    Sets up the first row of the month table with the day names
                    depending on the first day of the week.
    '''
    day_set = ['Monday', 'Tuesday', 'Wedensday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    # set up days depending on first day of the week, zero being monday.
    day_pointer = first_day
    days = [[day_set[(day_pointer + day_of_week) % DAYS_IN_WEEK] for day_of_week in range(DAYS_IN_WEEK)]]
    # set up the day header table
    week = Table(days, 7*[1.5*inch], 1*[0.25*inch])
    week.setStyle(TableStyle([('ALIGN', (0, 0), (-1, -1), 'CENTRE'),
                              ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                              ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.blue),
                              ('BACKGROUND', (0, 0), (-1, -1), colors.blue),
                              ('BOX', (0, 0), (-1, -1), 0.25, colors.blue),
                              ('TEXTCOLOR', (0, 0), (-1, -1), colors.white),
                              ('FONTSIZE', (0, 0), (-1, -1), 14),
                             ]))
    return week



def make_data(month):
    '''
    Method:         make_data
    Parameters:     None
    Returns:        None
    Description:    produce data for each day of the month, if it exists.
    '''
    blank_days = calendar.monthrange(YEAR, month)[0]
    days_in_month = calendar.monthrange(YEAR, month)[1]
    date = - blank_days
    if days_in_month + blank_days > (DAYS_IN_WEEK * 5):
        weeks_in_month = 6
    else:
        weeks_in_month = 5

    data = []
    data.append(build_week(month, date))
    data.append(build_week(month, date + DAYS_IN_WEEK))
    data.append(build_week(month, date + DAYS_IN_WEEK * 2))
    data.append(build_week(month, date + DAYS_IN_WEEK * 3))
    data.append(build_week(month, date + DAYS_IN_WEEK * 4))
    if 6 == weeks_in_month:
        data.append(build_week(month, date + DAYS_IN_WEEK * 5))

    # output to table
    week_data = Table(data, 7*[1.5*inch], weeks_in_month*[1.0*inch])
    week_data.setStyle(TableStyle([('ALIGN', (0, 0), (-1, -1), 'RIGHT'),
                                   ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                                   ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.blue),
                                   ('BACKGROUND', (5, 0), (-1, -1), colors.lavender),
                                   ('TEXTCOLOR', (0, 0), (-1, -1), colors.blue),
                                   ('BOX', (0, 0), (-1, -1), 0.25, colors.blue),
                                   ('FONTSIZE', (0, 0), (-1, -1), 13),
                                  ]))
    return week_data


def build_week(month, date):
    '''
    Method:         build_week
    Parameters:     data - date of first week day
    Returns:        list of week
    Description:
    '''
    days_in_month = calendar.monthrange(YEAR, month)[1]
    week = []
    # not using indexer _day_in_week
    for _day_in_week in range(DAYS_IN_WEEK):
        if date < days_in_month:
            date += 1
            if date > 0:
                day_data = get_calendar_data(month, date)
                day_data_str = [''.join(str(day_dat + '\n')) for day_dat in day_data]
                print ''.join(day_data_str)
                week.append(''.join(str(date) + '\n' + ''.join((day_data_str)) ))
            else:
                week.append('')
        else:
            week.append('')
    return week


def get_calendar_data(month, day):
    '''
    Method:         get_calendar_data
    Parameters:     Month and day
    Returns:        The compiled data.
    Description:    getter compiles birthdays, anivarsaries and appointments for a given month-day.
    '''
    cal_data = CalData()
    results = sort_date_lists(month, day, cal_data.bank_days)
    results += sort_date_lists(month, day, cal_data.birthdays)
    results += sort_date_lists(month, day, cal_data.aniversaries)
    results += sort_date_lists(month, day, cal_data.appointments)
    return results


def sort_date_lists(month, day, list_to_sort):
    '''
    Method:         sort_date_lists
    Parameters:     Month and day
    Returns:        The compiled data.
    Description:    gets month then day data from list_to_sort.
    '''
    # collect entries for month from the list to sort
    month_list = [each_month for each_month in list_to_sort if str(month) == each_month['month']]
    # collect day from the month list
    day_list = [each_day for each_day in month_list if str(day) == each_day['day']]
    return [data['name'] + delta_years(data['year']) for data in day_list]


def delta_years(year):
    '''
    Method:         delta_years
    Parameters:     year represents the year to delta
    Returns:        The compiled data.
    Description:    Helper calculates delta from YEAR to year
    '''
    if year > 0:
        return ' (' + str(YEAR - year) + ')'
    else:
        return ''


if __name__ == '__main__':
    main()
print "PDF created!"

