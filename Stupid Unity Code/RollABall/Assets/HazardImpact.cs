using System.Collections;
using System.Collections.Generic;
using UnityEngine;




public class HazardImpact : MonoBehaviour
{
    // Start is called before the first frame update
    private void OnTriggerEnter(Collider other)
    {
        GameObject ob = other.gameObject;
        if (ob.GetComponentInChildren<PlayerMovement>().breakWall)
        {
            ob.GetComponentInChildren<PlayerMovement>().breakWall = false;
            this.gameObject.SetActive(false);
            ob.GetComponentInChildren<Rigidbody>().velocity = new Vector3(0, 0, 0);
            ob.GetComponent<Renderer>().material.color = new Color(0.04513669f, 1f, 0f);
            Vars.disabledList.Add(this.gameObject);

        }
        else
        {

            deathReset(ob);
        }

        
    }

    public static void deathReset(GameObject ob)
    {
        foreach (GameObject obj in Vars.disabledList.ToArray())
        {
            obj.SetActive(true);
            Vars.disabledList.Remove(obj);
        }

        ob.transform.position = new Vector3(-20, 7, (OnCollision.currentLevel - 1) * -150);
        ob.GetComponentInChildren<PlayerMovement>().resetSpeed();
        ob.GetComponentInChildren<Rigidbody>().velocity = new Vector3(0, 0, 0);


        RectTransform life = (RectTransform) Vars.hpList[Vars.hpList.Count - 1];
        life.gameObject.SetActive(false);
        Vars.hpList.Remove(life);

        if(Vars.hpList.Count <= 0)
        {
            GameObject deadText = GameObject.Find("DeadText");
            Vars.showElementText(deadText);
            PlayerMovement.hudActive = true;

            Debug.Log("GameOver");
        }
    }
}
