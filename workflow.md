URL Redirect Workflow
=====================

- Open the Sirsi list in OpenRefine
- Run the cleanUpURL.grel code to clean up the URL column
- If the number of records is large (it takes 24 hours to process 10,000 URLs
	- Export as CSV
	- Break the CSV into batches using splitCSV/csv_splitter.py
	- Import a batch back into OpenRefine
- Exclude (facet) any titles that don't need redirects. This reduces the amount of time it'll take to process
- Click the arrow next to the URL header, choose `Edit column` > `Add column based on this column...`
- Choose `Python/Jython` from the `Language` dropdown
- Copy and paste the text in jythonURLRedirect.py into the text box, and press OK
- Remove current facet, and facet the new column by clicking the arrow > `Facet` > `Customized facets` > `Facet by blank`, and choose `True` on the left
- Click the arrow again, choose `Edit cells` > `Transform...`
- Write `cells["URL"].value` in the text box to fill in any blank cells with URLs from the URL column
- Delete the `URL` column, rename new column `URL`
- Export as CSV
