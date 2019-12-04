using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class OnCollision : MonoBehaviour
{
    public static int currentLevel = 1;
    const int maxLevel = 5;

    public bool cheat;
    public int cheatLevel;


    private void Start()
    {
        if (cheat)
        {
            currentLevel = cheatLevel;
            
        }
    }

    void OnTriggerEnter(Collider other)
    {
        if (currentLevel != maxLevel)
        {
            PlayerMovement.freezeGame(true);
            other.gameObject.GetComponentInChildren<PlayerMovement>().resetSpeed();
            Follower.zCor = currentLevel * -150;
            GameObject go = GameObject.Find("Player");
            Rigidbody rb = go.GetComponentInChildren<Rigidbody>();
            rb.velocity = new Vector3(0, 0, 0);
            go.transform.position = new Vector3(-20, 7, currentLevel * -150);
            rb.velocity = new Vector3(0, 0, 0);
            currentLevel++;

            GameObject.Find("LevelCounter").GetComponent<UnityEngine.UI.Text>().text = "Level: " + currentLevel;


            Vars.timeTaken += (int) Vars.levelTime;
            showCompleteText(currentLevel - 1, Vars.levelTime);
            Vars.resetTimer();
            PlayerMovement.hudActive = true;

            Vars.startHUDWait();
            PlayerMovement.freezeGame(false);
        }
        else
        {
            Vars.timeTaken += (int)Vars.levelTime;

            showElementText(GameObject.Find("CompleteText"));
            PlayerMovement.hudActive = true;
            PlayerMovement.freezeGame(true);
            other.gameObject.GetComponentInChildren<Rigidbody>().velocity = new Vector3(0, 0, 0);


            GameObject.Find("GameTimer").GetComponent<UnityEngine.UI.Text>().text = "Game completed in " + Mathf.Round(Vars.timeTaken) +
                " seconds";
            showElementText(GameObject.Find("GameTimer"));

        }

    }

    void showCompleteText(int level, float timeCompleted)
    {
        GameObject textParent = GameObject.Find("LevelText");

        GameObject completeText = textParent.transform.Find("LevelCompleteText").gameObject;
        completeText.GetComponent<UnityEngine.UI.Text>().text = "Level " + level + " Complete!";
        showElementText(completeText);

        GameObject timeText = textParent.transform.Find("CompleteTimer").gameObject;
        timeText.GetComponent<UnityEngine.UI.Text>().text = "Course completed in " + Mathf.Round(timeCompleted) + " seconds";
        showElementText(timeText);
    }

    void showElementText(GameObject gObject)
    {
        gObject.GetComponent<UnityEngine.UI.Text>().color = new Color(
            gObject.GetComponent<UnityEngine.UI.Text>().color.r, gObject.GetComponent<UnityEngine.UI.Text>().color.g,
            gObject.GetComponent<UnityEngine.UI.Text>().color.b, 1);
    }

    void hideElementText(GameObject gObject)
    {
        gObject.GetComponent<UnityEngine.UI.Text>().color = new Color(
            gObject.GetComponent<UnityEngine.UI.Text>().color.r, gObject.GetComponent<UnityEngine.UI.Text>().color.g,
            gObject.GetComponent<UnityEngine.UI.Text>().color.b, 0);
    }
}
