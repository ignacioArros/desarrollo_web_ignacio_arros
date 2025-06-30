package springboot_app.springboot_app.models;

import jakarta.persistence.*;

@Entity
@Table(name = "actividad_tema")
public class ActividadTema {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @Column(name = "tema", nullable = false)
    private String tema;

    @Column(name = "glosa_otro")
    private String glosaOtro;

    @Column(name = "actividad_id", nullable = false)
    private Integer actividadId;

    // Getters y setters
    public Integer getId() { return id; }
    public void setId(Integer id) { this.id = id; }

    public String getTema() { return tema; }
    public void setTema(String tema) { this.tema = tema; }

    public String getGlosaOtro() { return glosaOtro; }
    public void setGlosaOtro(String glosaOtro) { this.glosaOtro = glosaOtro; }

    public Integer getActividadId() { return actividadId; }
    public void setActividadId(Integer actividadId) { this.actividadId = actividadId; }
}
