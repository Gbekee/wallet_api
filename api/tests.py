from django.test import TestCase

# Create your tests here.
x={
    "email": "gbeke@gmail.com",
    "wallets": [
        {
            "num": 811329990,
            "balance": "19.80",
            "card": 5613819519671895,
            "user": 1,
            "debits": [
                {
                    "id": 11,
                    "receiver": 1,
                    "initiator": 1,
                    "amount": "20.000",
                    "description": "test",
                    "time": "2024-06-19T21:06:21.087121Z"
                },
                {
                    "id": 12,
                    "receiver": 2,
                    "initiator": 1,
                    "amount": "20.000",
                    "description": "test",
                    "time": "2024-06-19T21:06:59.751323Z"
                },
                {
                    "id": 13,
                    "receiver": 2,
                    "initiator": 1,
                    "amount": "20.000",
                    "description": "test",
                    "time": "2024-06-19T21:11:02.803016Z"
                },
                {
                    "id": 14,
                    "receiver": 2,
                    "initiator": 1,
                    "amount": "20.000",
                    "description": "test",
                    "time": "2024-06-19T21:11:23.070295Z"
                },
                {
                    "id": 15,
                    "receiver": 2,
                    "initiator": 1,
                    "amount": "20.000",
                    "description": "test",
                    "time": "2024-06-19T21:12:07.422818Z"
                },
                {
                    "id": 18,
                    "receiver": 3,
                    "initiator": 1,
                    "amount": "10.000",
                    "description": "test",
                    "time": "2024-06-19T21:13:34.400130Z"
                },
                {
                    "id": 20,
                    "receiver": 1,
                    "initiator": 1,
                    "amount": "20.000",
                    "description": "test",
                    "time": "2024-06-19T21:34:59.629152Z"
                },
                {
                    "id": 21,
                    "receiver": 2,
                    "initiator": 1,
                    "amount": "20.000",
                    "description": "test",
                    "time": "2024-06-19T21:35:06.620586Z"
                },
                {
                    "id": 22,
                    "receiver": 3,
                    "initiator": 1,
                    "amount": "20.000",
                    "description": "test",
                    "time": "2024-06-19T21:35:38.214966Z"
                },
                {
                    "id": 25,
                    "receiver": 2,
                    "initiator": 1,
                    "amount": "10.000",
                    "description": "test",
                    "time": "2024-06-19T21:38:21.490375Z"
                },
                {
                    "id": 29,
                    "receiver": 2,
                    "initiator": 1,
                    "amount": "10.202",
                    "description": "test",
                    "time": "2024-06-19T22:02:28.011192Z"
                },
                {
                    "id": 32,
                    "receiver": 2,
                    "initiator": 1,
                    "amount": "10.000",
                    "description": "test",
                    "time": "2024-06-20T03:55:01.801905Z"
                },
                {
                    "id": 36,
                    "receiver": 2,
                    "initiator": 1,
                    "amount": "12.100",
                    "description": "test",
                    "time": "2024-06-20T03:59:31.480036Z"
                }
            ],
            "credits": [
                {
                    "id": 3,
                    "receiver": 1,
                    "initiator": 3,
                    "amount": "100.000",
                    "description": "test",
                    "time": "2024-06-19T20:22:58.129153Z"
                },
                {
                    "id": 4,
                    "receiver": 1,
                    "initiator": 3,
                    "amount": "100.000",
                    "description": "test",
                    "time": "2024-06-19T20:52:36.837597Z"
                },
                {
                    "id": 5,
                    "receiver": 1,
                    "initiator": 3,
                    "amount": "120.000",
                    "description": "test",
                    "time": "2024-06-19T20:57:21.132914Z"
                },
                {
                    "id": 7,
                    "receiver": 1,
                    "initiator": 2,
                    "amount": "100.000",
                    "description": "test",
                    "time": "2024-06-19T20:59:27.685674Z"
                },
                {
                    "id": 8,
                    "receiver": 1,
                    "initiator": 2,
                    "amount": "20.000",
                    "description": "test",
                    "time": "2024-06-19T21:01:16.685970Z"
                },
                {
                    "id": 9,
                    "receiver": 1,
                    "initiator": 3,
                    "amount": "10.000",
                    "description": "test",
                    "time": "2024-06-19T21:03:57.591662Z"
                },
                {
                    "id": 10,
                    "receiver": 1,
                    "initiator": 3,
                    "amount": "10.000",
                    "description": "test",
                    "time": "2024-06-19T21:04:56.700222Z"
                },
                {
                    "id": 11,
                    "receiver": 1,
                    "initiator": 1,
                    "amount": "20.000",
                    "description": "test",
                    "time": "2024-06-19T21:06:21.087121Z"
                },
                {
                    "id": 16,
                    "receiver": 1,
                    "initiator": 3,
                    "amount": "10.000",
                    "description": "test",
                    "time": "2024-06-19T21:12:29.865282Z"
                },
                {
                    "id": 17,
                    "receiver": 1,
                    "initiator": 2,
                    "amount": "10.000",
                    "description": "test",
                    "time": "2024-06-19T21:12:57.162842Z"
                },
                {
                    "id": 19,
                    "receiver": 1,
                    "initiator": 2,
                    "amount": "20.000",
                    "description": "test",
                    "time": "2024-06-19T21:34:52.578676Z"
                },
                {
                    "id": 20,
                    "receiver": 1,
                    "initiator": 1,
                    "amount": "20.000",
                    "description": "test",
                    "time": "2024-06-19T21:34:59.629152Z"
                },
                {
                    "id": 24,
                    "receiver": 1,
                    "initiator": 3,
                    "amount": "10.000",
                    "description": "test",
                    "time": "2024-06-19T21:37:40.260870Z"
                },
                {
                    "id": 27,
                    "receiver": 1,
                    "initiator": 3,
                    "amount": "20.000",
                    "description": "test",
                    "time": "2024-06-19T22:01:32.485578Z"
                },
                {
                    "id": 28,
                    "receiver": 1,
                    "initiator": 2,
                    "amount": "10.200",
                    "description": "test",
                    "time": "2024-06-19T22:01:56.365819Z"
                },
                {
                    "id": 37,
                    "receiver": 1,
                    "initiator": 2,
                    "amount": "10.000",
                    "description": "charity",
                    "time": "2024-06-21T00:08:32.743780Z"
                }
            ]
        }
    ],
    "name": "Gbeke Oye"
}
print(x['wallets'][0]['debits'][1]['amount'])