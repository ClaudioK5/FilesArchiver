This Python script allows users to archive files inside a source folder which are older than a specified number of days. The script won't remove or modify any of the files, ensuring data integrity.

Features:
- Archive Management: Archives files older than a given threshold (in days) to a dedicated archive folder inside the source directory;
- Logging: Each movement action is recorded in a log file stored in a log folder inside the source directory, providing a clear record of archived files.
- Lightweight: Uses only Python's built-in libraries, making it easy to use without external dependencies.

In order to use FilesArchiver, initialize it from the command line with the specified folder paths. The tool uses argparse to accept input parameters for the source folder and the number of days as the threshold.
