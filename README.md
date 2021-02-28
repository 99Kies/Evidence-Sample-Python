# Evidence

## API

### /new_evidence

接口定义：创建新存证

| 标题         | 描述             |
| ------------ | ---------------- |
| 接口路径     | /new_evidence    |
| Method       | GET / POST       |
| Content-Type | application/json |

接口入参：

| Key            | Value                                                        | Required |
| -------------- | ------------------------------------------------------------ | -------- |
| privkey        | "d6f8c8f9106835ccc8f8d0bbc4b5bf32ff5f8941e69f9f50d075684d10dda7be" | Y        |
| evidenceString | "hello, evidence"                                            | Y        |

返回内容：

```json
{
    "result": [
        {
            "address": "0x8fdb986c42f788e77f236d0bf77aaf753c147972",
            "data": "0x0000000000000000000000000000000000000000000000000000000000000040000000000000000000000000a2a9d06c3478778e2302bac12115c128334915f4000000000000000000000000000000000000000000000000000000000000000f68656c6c6f2c2065766964656e63650000000000000000000000000000000000",
            "topics": [
                "0x68a6f2dd22a3385ea4d4fd8b590e4890ff82d99853226c67df889e74dda33e67"
            ]
        },
        {
            "address": "0xa2a9d06c3478778e2302bac12115c128334915f4",
            "data": "0x0000000000000000000000008fdb986c42f788e77f236d0bf77aaf753c147972",
            "topics": [
                "0x8b94c7f6b3fadc764673ea85b4bfef3e17ce928d13e51b818ddfa891ad0f1fcc"
            ]
        }
    ]
}
```



### /evidence/<address\>

接口定义：通过evidence地址获取具体内容。


| 标题         | 描述                 |
| ------------ | -------------------- |
| 接口路径     | /evidence/<address\> |
| Method       | GET / POST           |
| Content-Type | application/json     |

`curl http://127.0.0.1:5000/evidence/0x8fdb986c42f788e77f236d0bf77aaf753c147972`

返回内容：

```json
{
    "result": [
        "hello, evidence",
        [
            "0x28b7a9da9f3a92e139b58181aee04d0720cdd767",
            "0x6aa005f1bdf1d9bd003b6fb9838c0f91df0c9ac8"
        ],
        [
            "0x28b7a9da9f3a92e139b58181aee04d0720cdd767"
        ]
    ]
}
```

### /addsignatures

接口定义：添加存证签名

| 标题         | 描述             |
| ------------ | ---------------- |
| 接口路径     | /addsignatures   |
| Method       | GET / POST       |
| Content-Type | application/json |

接口入参：

| Key             | Value                                                        | Required |
| --------------- | ------------------------------------------------------------ | -------- |
| privkey         | "619834a32f41fc9dce7809c3063070af3d78fac577a0c12705984eed0b1a3cb" | Y        |
| evidenceAddress | "0x8fdb986c42f788e77f236d0bf77aaf753c147972"                 | Y        |

返回内容：

```json
{
    "result": [
        {
            "address": "0x8fdb986c42f788e77f236d0bf77aaf753c147972",
            "data": "0x0000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000f68656c6c6f2c2065766964656e63650000000000000000000000000000000000",
            "topics": [
                "0x20816d1858bab038efc3fee7f47dbb0de0e5dc3425549996d36d148220973e02"
            ]
        }
    ]
}
```

### /verifysigner

接口定义：验证是否存在该用户。

| 标题         | 描述             |
| ------------ | ---------------- |
| 接口路径     | /verifysigner    |
| Method       | GET / POST       |
| Content-Type | application/json |

接口入参：

| Key           | Value                                        | Required |
| ------------- | -------------------------------------------- | -------- |
| signerAddress | "0x6aa005f1bdf1d9bd003b6fb9838c0f91df0c9ac8" | Y        |

返回内容：

```json
{
    "result": true
}
```



### /signer/<index\>

接口定义：通过下标索引获取对应的账户地址。


| 标题     | 描述             |
| -------- | ---------------- |
| 接口路径 | /signer/<index\> |
| Method   | GET              |

`curl http://127.0.0.1:5000/signer/1`

返回内容：

```json
{
    "address": "0x6aa005f1bdf1d9bd003b6fb9838c0f91df0c9ac8"
}
```





### /signer/lists

接口定义：列出所有的用户地址。


| 标题     | 描述          |
| -------- | ------------- |
| 接口路径 | /signer/lists |
| Method   | GET           |

`curl http://127.0.0.1:5000/singer/lists`

返回内容：

```json
{
    "signers": [
        "0x28b7a9da9f3a92e139b58181aee04d0720cdd767",
        "0x6aa005f1bdf1d9bd003b6fb9838c0f91df0c9ac8"
    ]
}
```



### /signer/size

接口定义：获取用户地址列表的大小。


| 标题     | 描述         |
| -------- | ------------ |
| 接口路径 | /signer/size |
| Method   | GET          |

`curl http://127.0.0.1:5000/singer/size`

返回内容：

```json
{
    "size": 2
}
```



## Evidence类

示例

```python
from evidence_contract import Evidence_Contract
contract_address = "0xa2a9d06c3478778e2302bac12115c128334915f4"
privkey = "d6f8c8f9106835ccc8f8d0bbc4b5bf32ff5f8941e69f9f50d075684d10dda7be"
evidence_string = "hello, evidence"

evidence = Evidence_Contract(contract_address)
evidence.client.set_account_by_privkey(privkey)
new_evi = evidence.new_evidence_by_evi(evidence_string)
```

