# Welcome to repository of the Panel Dashboard App Template for Numerous

This repository contains the Panel Dashboard App Template. It was created by the Numerous team to be used as a template for creating new selection apps through the Numerous platform.

To deploy this app you can go to the [Numerous Platform](https://numerous.com/platform) and click create new app and select the dashboard app template.

To download the app after you have created it on the Numerous Platform, you can click install the Numerous CLI with:

```bash
pip install numerous
```

and then run:

```bash
numerous download -o <your organization> -a <app slug>
```

Alternatively, you can clone this repository continue working on it, before pushing it to the Numerous Platform.

## Local Development

To run the app locally, you can run the following command:

```bash
pip install .
panel serve app.py
```


