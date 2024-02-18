command for the win challenge files

My File naming convention
=========================
1. The first nine tasks files begin with '0-first_9_tasks' followed by the task number. E.g "0-first_9_tasks_task_1.png"
2. The next nine tasks files begin with '1-next_9_tasks' followed by the task number. E.g "1-next_9_tasks_task_1.png"
3. The next nine tasks files begin with '2-next_9_tasks' followed by the task number. E.g "2-next_9_tasks_task_1.png"


Steps in using the SFTP command-line tool
========================================

1. Log into your intranet
2. Click on the sanbox icon from the sidebar
3. Run your sandbox if its idle
4. Click on SFTP to copy the sftp command
5. Open your terminal
6. Paste your copied commands and press Enter. ( Type yes when prompted)
7. Copy the password from the sandbox page in your intranet
8. Paste it in the terminal when prompted for password. (Note: you will not see the pasted password for security purposes)
9. Navigate to the directory where you want to upload the screenshots to
10. Upload your files recursively using the put command and the -r flag followed by the path to the files on your local machine and hit Enter.
11. You should see a confirmation message indicating that the directory and its contents have been uploaded successfully.
12. Type 'exit' and hit Enter to exit the sftp session

Thank You
