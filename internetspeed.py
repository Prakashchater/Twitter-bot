from time import sleep
class x:
    def __init__(self,driver):
        self.driver = driver
        speed_test = ".overall-progress"
        download_speed_css = ".download-speed"
        upload_speed_css = ".upload-speed"
        in_progress = True
        while in_progress:
            progress = self.driver.find_element_by_css_selector(speed_test)
            if progress.startswith("Your speed test has completed"):
                download_result = self.driver.find_element_by_css_selector(download_speed_css)
                upload_result = self.driver.find_element_by_css_selector(upload_speed_css)
                print(
                    f"Your download speed is {download_result.text}MBits/s and your upload speed is {upload_result.text} MBits/s.")
                in_progress = False
            else:
                sleep(5)
