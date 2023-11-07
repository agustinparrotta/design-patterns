
import logging

logging.basicConfig(level='INFO')

def get_text():
    """Method to get the text of file"""
    return "plain_text"
 
def get_xml():
    """Method to get the xml version of file""" 
    return "xml"
 
def get_pdf():
    """Method to get the pdf version of file"""
    return "pdf"
 
def get_csv():
    """Method to get the csv version of file"""
    return "csv"
 
def convert_to_text(data):
    """Method used to convert the data into text format"""
    logging.info("[CONVERT]")
    return "{} as text".format(data)
 
def saver():
    """Method used to save the data"""
    logging.info("[SAVE]")
 
def template_function(getter, converter = False, to_save = False):
    """Helper function named as template_function"""

    # Input data from getter
    data = getter()
    logging.info("Got `{}`".format(data))
 
    if len(data) <= 3 and converter:
        data = converter(data)
    else:
        logging.info("Skip conversion")
     
    # Saves the data only if user want to save it
    if to_save:
        saver()
 
    logging.info("`{}` was processed".format(data))
 
def main():
    
    template_function(get_text, to_save = True)
 
    template_function(get_pdf, converter = convert_to_text)
 
    template_function(get_csv, to_save = True)
 
    template_function(get_xml, to_save = True)

if __name__ == "__main__":
    main()