from pubsub import pub

FOOTBALL_TOPIC = 'football'
CHESS_TOPIC = 'chess'


def listener_alice(arg):
    print("Alice receive news about", arg['headline'])
    print(arg['news'])
    print()

def listener_bob(arg):
    print("Bob receives news about", arg['headline'])
    print(arg['news'])
    print()


# register listener
pub.subscribe(listener_alice, FOOTBALL_TOPIC)
pub.subscribe(listener_alice, CHESS_TOPIC)
pub.subscribe(listener_bob, FOOTBALL_TOPIC)

# send messages to all listeners of topics
pub.sendMessage(FOOTBALL_TOPIC, arg={'headline': 'Ronaldo', 'news': 'Sold for $1M'})
pub.sendMessage(CHESS_TOPIC, arg={'headline': 'AI', 'news': 'AlphaZero beats grandmaster Carlsen'})