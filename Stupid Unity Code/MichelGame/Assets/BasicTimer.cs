using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class BasicTimer : MonoBehaviour
{

    public float timeRemaining = 3.0f;

    private Text timer;

    GameObject[] targets;

    // Start is called before the first frame update
    void Start()
    {
        timer = GetComponent<Text>();
        targets = GameObject.FindGameObjectsWithTag("Target");

    }

    // Update is called once per frame
    void Update()
    {

        if(timeRemaining < 0)
        {
            return;
        }

        timeRemaining -= Time.deltaTime;

        int minutes = Mathf.FloorToInt(timeRemaining / 60f);
        int seconds = Mathf.RoundToInt(timeRemaining % 60f);

        string formatedSeconds = seconds.ToString();

        if (seconds == 60)
        {
            seconds = 0;
            minutes += 1;
        }

        timer.text = minutes.ToString("00") + ":" + seconds.ToString("00");

        if(timeRemaining <= 0)
        {

            GameObject.Find("GameOverText").GetComponent<Text>().color = new Color(1, 0.8386418f, 0, 1);
            timer.text = "00:00";
            foreach (GameObject g in targets){
                g.GetComponent<TargetSpawn>().freeze = true;
            }
        }
    }
}
