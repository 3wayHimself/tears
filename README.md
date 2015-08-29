# tears

> A bottle of Tears

**tears** (support Python3 only) is a pure clean blog (engine), powered by bottle.

I love [next](https://github.com/iissnan/hexo-theme-next) cause you may found some dim shapes of it's layout.

[Demo Preview | 预览](http://sinux.cc/)

![](https://github.com/shnode/tears/raw/master/demo.png)


- tears keep simple and clean both in interface and backend, focus on content
- all backend code in one file to follow bottle's style
- posts with raw markdown files, just back up `source` folder periodically
- contains a `post_engine` which check .md files and insert them into mongoDB
- work best in the latest desktop and mobile browsers (because of bootstrap)

## Usage

suppose you have mongodb installed in your system

```bash
    pip install -r requirements.txt
```

generate `/source`:

```
    python post_engine.py -i
```

create your post:

```
    python post_engine.py -c [your file name]
```

then edit your post markdown file, you must follow the form below, or tears will give you syntax error:

```
    title: this is a example
    date: 2016-03-13 16:44:00
    categories: Language
    tags:
    - Ruby
    - Dynamic-programming-language

    ---

    your content

```

finally we generate the post and insert into mongoDB, and access the url:

```
    python post_engine.py -g

    open "http://localhost:8080"
```

you may modify some personal information

## Contribute

Any advice is welcomed

## License

MIT
