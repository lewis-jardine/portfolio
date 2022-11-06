# /test

## GET

API returns:

```
{"message": "Hello World"}
```

# /upload

## POST

Hardware sends:

```
File: binary image
```

API returns:

```
{
  metadata: {
    format: str (image file extension),
    height: int,
    width: int
  },
  modelVersion: str (azure OD model name),
  objects: [{
    confidence: int,
    object: str,
    rectangle: {
      x: int,
      y: int,
      w: int,
      h: int
    },
    parent: {
      confidence: int,
      object: str,
      parent: {...}
    }
  }],
  requestId: str,
  time: str (datetime format),
  url: str
}
```
