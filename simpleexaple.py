'''
simple example with await
'''

import asyncio
import aiomysql


async def test_example(loop):
    conn = await aiomysql.connect(host='127.0.0.1', port=3306,
                                  user='root', password='passwordabc', db='test',    # my sql password is passwordabc, the exitings db is test
                                  loop=loop)

    async with conn.cursor() as cur:
        await cur.execute('select * from user where id = %s', ('1',))
        print(cur.description)
        r = await cur.fetchall()
        print(r)
    conn.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(test_example(loop))