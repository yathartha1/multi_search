# Multi Search

Search selected text or word on sites of your choice. This automates the manual work of copying your selection and pasting it to the browser search bar.

Utilities Provided:
* Provides a Popup where you can select the site you want to search on. Default ones are - Google, StackOverflow and AskUbuntu.
* Customizable Site Options.
* Ways to Open the Popup:
    * Right clicking on a selection.
    * Using the Default Key Combination of Ctrl+Shift+Z.

## Installation

Recommended With [Package Control](https://packagecontrol.io):

1. Run “Package Control: Install Package” command, find and install `Multi Search` plugin.
2. Restart SublimeText editor

Manually:

1. Clone this git repository into your packages folder (in SublimeText, Preferences -> Browse Packages to open this folder)
2. Restart SublimeText editor

## Adding More Sites

Edit the settings by going to Preferences -> Package Settings -> Multi Search -> Settings - User

```js
{
    "domains": ["Google Search", "Stack Overflow Search", "Ask Ubuntu Search"],
    "domain_urls": ["https://www.google.com", "https://stackoverflow.com", "https://askubuntu.com"]
}
```

The domains and domain_urls have one to one relationship, the value at a specific index of the domain should have correspond to the value at the specific index of the domain_urls.



