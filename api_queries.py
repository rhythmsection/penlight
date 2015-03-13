def basic_phrase_query(data):    
    all_the_information = []
    speakers = []
    quotes = []
    for n in range(0, len(data['results'])):
        if data['results'][n]['speaker_first'] and data['results'][n]['speaker_last']:
            speaker = data['results'][n]['speaker_first'] + " " + data['results'][n]['speaker_last'] + " (" + data['results'][n]['date'] + ")"
            speakers.append(speaker)
            quote = "Quote: "
            for paragraph in data['results'][n]['speaking']:
                quote = quote + paragraph + "\n\n"
            quotes.append(quote)
        else:
            speakers.append( "(" + data['results'][n]['date'] + ")" )
            quote = "Quote: "
            for paragraph in data['results'][n]['speaking']:
                quote = quote + paragraph + "\n\n"
            quotes.append(quote)
    quote_range = len(speakers)-2
    all_the_information.append(speakers)
    all_the_information.append(quotes)
    all_the_information.append(quote_range)

    return all_the_information
