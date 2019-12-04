using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class WallBreaker : MonoBehaviour
{
    // Start is called before the first frame update
    private void OnTriggerEnter(Collider other)
    {
        this.gameObject.SetActive(false);
        Vars.disabledList.Add(this.gameObject);
        GameObject go = other.gameObject;
        go.GetComponent<Renderer>().material.color = new Color(0.990566f, 0.9657303f, 0.09812211f); 
        go.GetComponentInChildren<PlayerMovement>().breakWall = true;
    }
}
