import functions as fn

assert(fn.check_greetings('hi') in greeting_response)
assert(fn.check_greetings('asdhufsacb') in else_response)


assert fn.OpenHours
assert fn.OpenHours('name', 'day', 'time', 'room')

assert isinstance(fn.test_oh, fn.OpenHours)

assert fn.test_oh.shopname == "Tapioca Express"
assert fn.test_oh.name == name
assert fn.test_oh.day == day
assert fn.test_oh.time == time
assert fn.test_oh.place == place

assert (fn.is_question('Hi?'))

fn.respond_question('What for?')