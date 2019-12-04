using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SpeedImpact : MonoBehaviour
{
    // Start is called before the first frame update
    private void OnTriggerEnter(Collider other)
    {

        other.gameObject.GetComponentInChildren<PlayerMovement>().setScrollSpeed(
            other.gameObject.GetComponentInChildren<PlayerMovement>().getScrollSpeed() * 2);
    }
}
