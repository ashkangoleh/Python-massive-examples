import faust


class Greeting(faust.Record):
    exchange =str
    base= str
    quote= str
    timeframe= str
    strategies= dict[dict[str]]

app = faust.App('strategist.matches', broker='kafka://arz.local:9093')
topic = app.topic('hello-topic', value_type=Greeting)

@app.agent(topic)
async def hello(greetings):
    async for greeting in greetings:
        print(f'Hello from {greeting.base} to {greeting.quote}')

@app.timer(interval=1.0)
async def example_sender(app):
    await hello.send(
        value=Greeting(from_name='Faust', to_name='you'),
    )

if __name__ == '__main__':
    app.main()