/**
 * This class is designed to be used to encode strings using the url encode
 * character change parameters. Some methods are designed to be used to add urls
 * to a url that accesses a web service API.
 *
 * This class was written, compiled, and git serviced on the Raspberry Pi Zero
 * using BlueJay IDE.
 *
 * @author Peteous
 * @version 0.0.1
 */
public class urlEncode
{
    /**
     * Internal method containing character change rules for url encoding
     *
     * @param  url  the String you want to url encode
     * @return      the encoded url
     */
    private String Encode(String url)
    {
        // replacement character requirements for url encode specifications
        url.replace("%","%25");
        url.replace("!","%21");
        url.replace("#","%23");
        url.replace("$","%24");
        url.replace("&","%26");
        url.replace("\'","%27");
        url.replace("(","%28");
        url.replace(")","%29");
        url.replace("*","%2A");
        url.replace("+","%2B");
        url.replace(",","%2C");
        url.replace("/","@2F");
        url.replace(":","%3A");
        url.replace(";","%3B");
        url.replace("=","%3D");
        url.replace("?","%3F");
        url.replace("@","%40");
        url.replace("[","%5B");
        url.replace("]","%5D");
        return url;
    }

    /**
     * Method for writing an encoded url externally, using private Encode method
     *
     * @param  url  the String you want to url encode
     * @return      the encoded url
     */
    public String write(String url)
    {
        url = this.Encode(url);
        return url;
    }

    /**
     * Method for writing encoded url appended to an API's URL
     *
     * @param  url  the String you want to url encode
     * @param  apiURL the String of the URL of the API that you want to
     *                interface with
     * @return      the encoded url attached to the end of the apiURL
     */
    public String write(String url, String apiURL)
    {
        url = this.Encode(url);
        url = "url=" + url;
        return apiURL+url;
    }

    /**
     * Method for writing encoded url appended to an API's URL with parameters
     *
     * @param  url  the String you want to url encode
     * @param  apiURL the String of the URL of the API that you want to
     *                interface with
     * @param  paramNames an array of strings with the names of the parameters
     * @param  paramData an array of strings with coresponding values of parameters
     * @return      the encoded parameters with url attached to the end of the apiURL
     */
    public String write(String url, String apiURL, String[] paramNames, String[] paramData)
    {
        url = this.Encode(url);
        url = "&url=" + url;
        apiURL += "?";
        String parameters = "";
        for(int index = 0; index < paramNames.length; index++)
        {
            paramData[index] = this.Encode(paramData[index]);
            if(index < 1)
            {
                parameters += paramNames[index] + "=" + paramData[index];
            }
            else
            {
                parameters += "&" + paramNames[index] + "=" + paramData[index];
            }
        }
        return apiURL+parameters+url;
    }

    /**
     * Method for writing encoded url with parameters
     *
     * @param  url  the String you want to url encode
     * @param  paramNames an array of strings with the names of the parameters
     * @param  paramData an array of strings with coresponding values of parameters
     * @return      the encoded parameters with url attached to the end of the apiURL
     */
    public String write(String url, String[] paramNames, String[] paramData)
    {
        url = this.Encode(url);
        url = "&url=" + url;
        String parameters = "";
        for(int index = 0; index < paramNames.length; index++)
        {
            paramData[index] = this.Encode(paramData[index]);
            if(index < 1)
            {
                parameters += paramNames[index] + "=" + paramData[index];
            }
            else
            {
                parameters += "&" + paramNames[index] + "=" + paramData[index];
            }
        }
        return parameters+url;
    }
}
