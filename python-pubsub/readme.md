learning the pubsub design pattern for graphql subscription

https://blog.finxter.com/publish-subscribe-pypubsub/

Message is the subject

senders send messages and listeners subscribe to the message stream.

every message has a topic. can define a hierachy of topics with parent topics and child topics. a parent topic is more generic, a child topic is less generic.

message data is the actual content of the message.

all sent messages are delivered to the listeners for that topic. can listen to all topics by registering to the root of all topics - the parent of all - ALL_TOPICS.

No guarantees regarding the ordering of message delivery. Messages can appear out of order but are delivered synchorounsly: before a message is devliered to the next listener, the previous listener must terminate its callablable listener function == we don't run multiple threads on each listener to to deliver the messages in parallel. Instead, we deliver the messages one listner at a time.

immutability: listeners shouldn't change the content of the message they receive

direction: one way. message sends the message to all listeners of this message. However, can pass a callback function into the message data to allow receivers of a message to respond to the message by calling the callback function.
