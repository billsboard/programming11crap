using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Vars : MonoBehaviour
{
    // Start is called before the first frame update
    static int level;
    public static ArrayList disabledList = new ArrayList();

    public static ArrayList hpList = new ArrayList();

    public static float levelTime;
    float waitTime;

    static bool startHUD;
    static bool startCount;

    float counter = 3.0f;

    static UnityEngine.UI.Text countText;

    public static int timeTaken;
    

    

    private void Start()
    {

        GameObject healthHUD = GameObject.FindGameObjectWithTag("HealthUI");

        for(int i = 0; i < healthHUD.transform.childCount; i++)
        {
            hpList.Add(healthHUD.transform.GetChild(i));

        }
    }

    private void Update()
    {
        levelTime += Time.deltaTime;

        if (startHUD)
        {
            waitTime += Time.deltaTime;


            counter -= Time.deltaTime;

            countText.text = counter.ToString("0");
            if (counter <= 1)
            {

                startHUD = false;
                GameObject textParent = GameObject.Find("LevelText");

                GameObject completeText = textParent.transform.Find("LevelCompleteText").gameObject;
                hideElementText(completeText);

                GameObject timerText = textParent.transform.Find("CompleteTimer").gameObject;
                hideElementText(timerText);

                counter = 3;
                startCount = false;
                hideElementText(countText.gameObject);
                PlayerMovement.hudActive = false;
            }
        }

        if (startCount)
        {

        }


    }

    public static void resetTimer()
    {
        levelTime = 0.0f;
    }

    public static void startHUDWait()
    {
        countText = GameObject.Find("Countdown").GetComponent<UnityEngine.UI.Text>();
        showElementText(countText.gameObject);
        startHUD = true;
    }

    void startCountdown()
    {

        startCount = true;
    }

    void hideElementText(GameObject gObject)
    {
        gObject.GetComponent<UnityEngine.UI.Text>().color = new Color(
            gObject.GetComponent<UnityEngine.UI.Text>().color.r, gObject.GetComponent<UnityEngine.UI.Text>().color.g,
            gObject.GetComponent<UnityEngine.UI.Text>().color.b, 0);
    }

    public static void showElementText(GameObject gObject)
    {
        gObject.GetComponent<UnityEngine.UI.Text>().color = new Color(
            gObject.GetComponent<UnityEngine.UI.Text>().color.r, gObject.GetComponent<UnityEngine.UI.Text>().color.g,
            gObject.GetComponent<UnityEngine.UI.Text>().color.b, 1);
    }
}
