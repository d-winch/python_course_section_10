# python_course_section_10

Uses volcanoes.txt to map volcanoes on a map. Icon colour is determined by volcano height.
`if elevation < 1500:
        return 'green'
    elif 1500 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'`

World.json is used to map countries
Colour is determined by population
`style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else
'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))`
