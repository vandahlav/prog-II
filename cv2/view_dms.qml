import QtQuick 2.14
import QtQuick.Controls 2.14

Column {
    Row {
        spacing: 3

        TextInput {
            id: d_input
            text: dms.stupne
            
            Binding {
                target: dms
                property: "stupne"
                value: d_input.text
            }
        }

        Label {
            text: "°"
        }
        TextInput {
            id: m_input
            text: dms.minuty
            
            Binding {
                target: dms
                property: "minuty"
                value: m_input.text
            }
        }
        Label {
                text: "'"
            }

        TextInput {
            id: s_input
            text: dms.sekundy
            
            Binding {
                target: dms
                property: "sekundy"
                value: s_input.text
            }
        }

        Label {
            text: "''"
        }

        Button {
            text: 'to float'
            onClicked: dms.prevod()
        }
    }
    Row {
        spacing: 3

        TextInput {
                id: v_input
                text: dms.vsechno

                Binding {
                    target: dms
                    property: "vsechno"
                    value: v_input.text
                }
            }
        Label {
            text: "°"
        }
            
        Button {
            text: 'to dms'
            onClicked: dms.prevod_2()
   
    }
        }
        
}
    