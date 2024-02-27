import { View, Text, StyleSheet, Image } from "react-native";


function Profile(){
    return(
        <View>
            <Image style={styles.imagem} source={{uri:"https://th.bing.com/th/id/R.cd5d96228cbc69aa82ce6528e23507b9?rik=O202LD571GPCxw&riu=http%3a%2f%2fwww.ebanataw.com.br%2froberto%2ffluvial%2flogocorinthiansp.jpg&ehk=00RklshctQofWe2zFNFbAfQkj2AsAvBBb7ZSwt9iQDY%3d&risl=&pid=ImgRaw&r=0"}}/>
        </View>
    )   

}

export default function Gallery() {
    return(
        <View style={styles.container}>
            <Profile/>
        </View>
    )
}

const styles = StyleSheet.create ({
    container: {
        flex: 1,
        backgroundColor: 'white',
        alignItems: 'center',
        justifyContent: 'center',
      },
    imagem: {
        height: 250,
        width: 250,
    }
});

