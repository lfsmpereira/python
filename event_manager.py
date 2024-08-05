from datetime import datetime
from pytz import timezone, all_timezones
import pytz

# Lista para armazenar eventos
events = []

def add_event(event_name, event_datetime_str, event_tz_str):
    try:
        # Converter a string de data e hora para um objeto datetime
        event_datetime = datetime.strptime(event_datetime_str, '%Y-%m-%d %H:%M')
        
        # Verificar se o fuso horário fornecido é válido
        if event_tz_str not in all_timezones:
            raise ValueError("Fuso horário inválido")

        # Criar objeto de fuso horário para o evento
        event_tz = timezone(event_tz_str)
        
        # Localizar o objeto datetime no fuso horário do evento
        event_datetime = event_tz.localize(event_datetime)
        
        # Adicionar o evento à lista de eventos
        events.append((event_name, event_datetime, event_tz_str))
        print(f"Evento '{event_name}' adicionado com sucesso.")
    except Exception as e:
        print(f"Erro ao adicionar evento: {e}")

def list_events(user_tz_str):
    try:
        # Verificar se o fuso horário do usuário é válido
        if user_tz_str not in all_timezones:
            raise ValueError("Fuso horário inválido")
        
        user_tz = timezone(user_tz_str)
        
        # Listar eventos com datas e horários convertidos
        for event_name, event_datetime, event_tz_str in events:
            user_event_datetime = event_datetime.astimezone(user_tz)
            print(f"Evento: {event_name}, Hora do Evento: {event_datetime.strftime('%Y-%m-%d %H:%M')} ({event_tz_str}), Hora Local: {user_event_datetime.strftime('%Y-%m-%d %H:%M')} ({user_tz_str})")
    except Exception as e:
        print(f"Erro ao listar eventos: {e}")

def remove_event(event_name):
    global events
    events = [event for event in events if event[0] != event_name]
    print(f"Evento '{event_name}' removido.")

# Exemplo de uso
add_event('Cerimônia de Abertura', '2024-07-26 20:00', 'Asia/Tokyo')
add_event('100m Masculino', '2024-08-01 10:00', 'Asia/Tokyo')
list_events('America/Sao_Paulo')
remove_event('Cerimônia de Abertura')
list_events('America/Sao_Paulo')
