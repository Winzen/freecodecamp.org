def add_time(start, duration, week=False):

    dia_semana = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    if "AM" in start:
        separador = start.split("AM")
        separador = separador[0].split(":")
    else:
        separador = start.split("PM")
        separador = separador[0].split(":")
        separador[0] = str(int(separador[0])+12)

    somas = duration.split(":")

    hora_final = ((int(separador[1])+int(somas[1])) // 60) + int(separador[0])+int(somas[0]) - 24 * ((int(separador[0]) + int(somas[0])) // 24)
    minuto_final = (int(separador[1]) + int(somas[1])) - 60 * ((int(separador[1])+int(somas[1])) // 60)

    dias = ((int(separador[0]) + int(somas[0])) // 24) + (hora_final // 24)

    semana = (dia_semana.index(str(week).title()) + dias) - 7 * ((dia_semana.index(str(week).title()) + dias) // 7) if week != False else ''
    display_dia = '(next day)' if dias < 2 else f'({dias:.0f} days later)'
    display_hora = hora_final if hora_final <= 12 else hora_final - 12
    print(hora_final)
    return f"{display_hora if display_hora != 0 else '12' }:{str(minuto_final).rjust(2,'0')} {'AM' if hora_final < 12 or hora_final == 24 else 'PM'}{', '+ dia_semana[semana] if week != False else ''}{' ' + display_dia if dias != 0 else ''}"



if __name__ == '__main__':
    print(add_time( "11:59 PM", "24:05"))
