# Zapiest

My own Zapier like workflows that leverage the APIs of various applications I interact with. 

# Pocket → CloudConvert → Google Drive

- Check for new entry in Pocket (Wait for it to be tagged for conversion)
- Convert webpage to PDF using CloudConvert
- Upload file to Google Drive

## Dependencies

**Pocket**

`pip install pocket`

**CloudConvert**

`pip install cloudconvert`

**Google Drive API Client**
Need to get credentials from Google by setting up a new application and receiving OAuth ID. Follow instructions @ [https://developers.google.com/drive/v2/web/quickstart/python](https://developers.google.com/drive/v2/web/quickstart/python) to get is working.

`pip install --upgrade google-api-python-client`

## Resources

[Search for Files and Team Drives | Drive REST API | Google Developers](https://developers.google.com/drive/v3/web/search-parameters)

[Supported MIME Types | Drive REST API | Google Developers](https://developers.google.com/drive/v3/web/mime-types)

[Open Files | Drive REST API | Google Developers](https://developers.google.com/drive/v3/web/integrate-open#open_files_using_the_open_with_contextual_menu)

---